from config import Config
from pymongo import MongoClient

client = MongoClient(Config.LOCAL_URI)

try:
    coll = client.sample_guides.comets
    # filter = {}
    # doc = {
    #     "$mul": {"radius": 1.60934}
    # }

    # filter = {
    #     "radius": {"$type": "double"}
    # }

    # doc = [
    #     {
    #         "$set": {
    #             "radius": {
    #                 "$round": ["$radius", 2]
    #             }
    #         }
    #     }
    # ]

    filter = {
        "radius": {
            "$exists": True,
            "$type": ["double", "int"]
        }
    }

    doc = [{
        "$set":{
            "radius":{
                "$round": ["$radius", 2]
            }
        }
    }]


    result = coll.update_many(filter, doc)
    print(result.modified_count)

    cursor = coll.find()
    for dos in cursor:
        print(f'Name: {dos["name"]}\nRadius: {dos["radius"]}')
except Exception as e:
    print(e)

client.close()
