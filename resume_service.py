from db import db
from datetime import datetime

resume_collection = db["resume_records"]

# ------------------
# GET ALL RESUME DATA
# ------------------
def get_resume():
    record = resume_collection.find_one({"user": "default"}, {"_id": 0})
    
    if not record:
        return {
            "summary": "No summary provided.",
            "experience": [],
            "education": [],
            "skills": [],
            "projects": [],
            "languages": [],
            "honors": [],
            "courses": []
        }
        
    return record


# ------------------
# SAVE ENTIRE RESUME
# ------------------
def save_resume(payload):
    # Ensure user key exists so we can query it
    payload["user"] = "default"
    
    # Upsert the entire resume document
    resume_collection.update_one(
        {"user": "default"},
        {"$set": payload},
        upsert=True
    )
    
    return payload
