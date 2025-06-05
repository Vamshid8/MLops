import os
from pymongo import MongoClient
import certifi

# MongoDB connection
mongo_db_url = os.getenv("MONGODB_URL")
if mongo_db_url is None:
    raise Exception("MONGODB_URL environment variable is not set")

# Connect to MongoDB
client = MongoClient(mongo_db_url, tlsCAFile=certifi.where())
db = client["usvisa1"]
collection = db["visa_dataset1"]

# Check if collection exists and has data
print(f"Collection names in database: {db.list_collection_names()}")
print(f"Number of documents in visa_dataset1 collection: {collection.count_documents({})}")

# Print first document if exists
if collection.count_documents({}) > 0:
    print("First document sample:")
    print(collection.find_one()) 