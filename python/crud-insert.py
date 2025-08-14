from pymongo import MongoClient
from config import Config

client = MongoClient(Config.LOCAL_URI)


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.sample_guides
    coll = db.comets
    docs = [
        {"name": "Halley's Comet", "officialName": "1P/Halley", "orbitalPeriod": 75, "radius": 3.4175, "mass": 2.2e14},
        {"name": "Wild2", "officialName": "81P/Wild", "orbitalPeriod": 6.41, "radius": 1.5534, "mass": 2.3e13},
        {"name": "Comet Hyakutake", "officialName": "C/1996 B2", "orbitalPeriod": 17000, "radius": 0.77671, "mass": 8.8e12},
    ]

    result = coll.insert_many(docs)
    print(result.inserted_ids)

except Exception as e:
    print(e)