from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv('../.env')

username = os.getenv('MONGO_ROOT_USERNAME')
password = os.getenv('MONGO_ROOT_PASSWORD')
cluster = os.getenv('MONGO_CLUSTER')



# Replace the uri string with your MongoDB deployment's connection string.
# uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0"
url = f"mongodb://{username}:{password}@localhost:27017/"
client = MongoClient(url)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.sample_guides
    coll = db.planets
    # cursor = coll.find({'hasRings': False, 'mainAtmosphere': 'Ar'})
    cursor = coll.find(
        {
            "$or": [
                {"orderFromSun": {"$gt": 7}},
                {"orderFromSun": {"$lt": 2}},
            ]
        }
    )

    for planet in cursor:
        print(planet['name'])
except Exception as e:
    print(e)


client.close()
