import pymongo
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client["ai_companion"]

# Define collections
reminders_collection = db["reminders"]
users_collection = db["users"]

def get_db():
    """Returns database instance"""
    return db
