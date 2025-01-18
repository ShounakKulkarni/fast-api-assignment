from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user1:user1pass@learn-fast-api.wvgqm.mongodb.net/?retryWrites=true&w=majority&appName=learn-fast-api"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.assignment
collection = db["user-data"]