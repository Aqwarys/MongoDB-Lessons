from dotenv import load_dotenv
import os

load_dotenv('../.env')

username = os.getenv('MONGO_ROOT_USERNAME')
password = os.getenv('MONGO_ROOT_PASSWORD')
cluster = os.getenv('MONGO_CLUSTER')

# Replace the uri string with your MongoDB deployment's connection string.
LINKS = {
    'REMOTE': f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0",
    'LOCAL': f"mongodb://{username}:{password}@localhost:27017/"
}