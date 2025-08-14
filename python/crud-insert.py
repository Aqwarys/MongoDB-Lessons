from pymongo import MongoClient
from config import Config

client = MongoClient(Config.LOCAL_URI)


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.sample_guides
    coll = db.comets

except Exception as e:
    print(e)