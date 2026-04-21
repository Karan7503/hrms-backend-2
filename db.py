from pymongo import MongoClient

# connect to local mongodb
client = MongoClient("mongodb://localhost:27017")

# database name
db = client["hrms"]

# collection name
attendance_collection = db["attendance"]

# new collection for conference room bookings
conference_collection = db["conference_bookings"]