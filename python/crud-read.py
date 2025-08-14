from pymongo import MongoClient
from config import LINKS



client = MongoClient(LINKS['LOCAL'])

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
