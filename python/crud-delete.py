from config import Config
from pymongo import MongoClient

client = MongoClient(Config.LOCAL_URI)

try:
    coll = client.sample_guides.comets
    doc = {
        "orbitalPeriod": {
            "$gt": 5,
            "$lt":85
        }
    }
    result = coll.delete_many(doc)

    print(result.deleted_count)
except Exception as e:
    print(e)


client.close()
