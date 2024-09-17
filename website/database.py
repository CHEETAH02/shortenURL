from pymongo.mongo_client import MongoClient
import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

uri = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.3fajycc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client['ShortenURL']
