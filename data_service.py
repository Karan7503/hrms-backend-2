from db import db

employee_collection = db["employee_data"]


def get_employee_data():
    record = employee_collection.find_one({"user": "default"}, {"_id": 0})
    if not record:
        return {
            "personal": {},
            "contact": {
                "work_email": "",
                "facebook": "",
                "contact_details": [],
                "communication_details": []
            },
            "medical": {
                "blood_group": "",
                "any_illness": "",
                "allergies": "",
                "previous_hospitalization": "",
                "emergency_contacts": []
            },
            "other": {
                "bank_pan_aadhar": [],
                "passport_details": [],
                "visa_details": []
            }
        }
    return record


def save_employee_data(payload):
    payload["user"] = "default"
    employee_collection.update_one(
        {"user": "default"},
        {"$set": payload},
        upsert=True
    )
    return payload
