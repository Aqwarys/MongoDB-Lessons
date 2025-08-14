from pymongo import MongoClient
from config import LINKS

client = MongoClient(LINKS['LOCAL'])


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.sample_guides
    coll = db.comets

except Exception as e:
    print(e)