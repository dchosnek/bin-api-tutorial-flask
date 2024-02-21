"""
Simple configuration of the Mongo database to set up an index (and force
uniqueness) on the email field.
"""

from pymongo import MongoClient

DATABASE_NAME = "mydatabase"
COLLECTION_NAME = "bins"


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# if the database does not exist, it will be created
db = client[DATABASE_NAME]

# if the collection does not exist, it will be created
collection = db[COLLECTION_NAME]

# create the index -- this is idempotent
collection.create_index([("email", 1)], unique=True)