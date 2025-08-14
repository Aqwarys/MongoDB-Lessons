from pymongo import MongoClient
from config import Config



client = MongoClient(Config.LOCAL_URI)

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
