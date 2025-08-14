import os
from dotenv import load_dotenv

load_dotenv('../.env')


class Config:
    MONGO_ROOT_USERNAME = os.getenv('MONGO_ROOT_USERNAME')
    MONGO_ROOT_PASSWORD = os.getenv('MONGO_ROOT_PASSWORD')
    MONGO_URL = os.getenv('MONGO_URL')

    REMOTE_URI =  f"mongodb+srv://{MONGO_ROOT_USERNAME}:{MONGO_ROOT_PASSWORD}@{MONGO_URL}/?retryWrites=true&w=majority&appName=Cluster0"
    LOCAL_URI = f"mongodb://{MONGO_ROOT_USERNAME}:{MONGO_ROOT_PASSWORD}@localhost:27017/"