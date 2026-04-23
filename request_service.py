# from data import requests_data
# from datetime import datetime


# def generate_request_no():

#     return f"REQ{len(requests_data)+1:03d}"


# def get_requests():

#     return requests_data


# def create_request(payload):

#     new_request = {

#         "request_no": generate_request_no(),

#         "owner": payload.get("owner", "Karan"),

#         "request_for": payload.get("request_for"),

#         "subject": payload.get("subject"),

#         "comments": payload.get("comments"),

#         "open_date": payload.get("open_date"),

#         "close_date": payload.get("close_date"),

#         "actual_closed_date": payload.get("actual_closed_date"),

#         "user_status": payload.get("user_status", "Open"),

#         "request_status": payload.get("request_status", "Pending"),

#         "report_to": payload.get("report_to"),

#         "response_status": "Pending",

#         "active": payload.get("active", True),

#         "created_at": datetime.now().isoformat()

#     }

#     requests_data.append(new_request)

#     return new_request


from db import db
from datetime import datetime

request_collection = db["requests"]


# ------------------
# GET REQUESTS
# ------------------
def get_requests():

    records = list(
        request_collection.find({}, {"_id": 0})
    )

    return records


# ------------------
# CREATE REQUEST
# ------------------
def create_request(payload):

    print("REQUEST PAYLOAD:", payload)

    record = {
        "request_no": int(datetime.now().timestamp()),

        "owner": payload.get("owner", "Karan"),

        "request_for": payload.get("request_for"),
        "subject": payload.get("subject"),
        "comments": payload.get("comments"),

        "open_date": payload.get("open_date"),
        "close_date": payload.get("close_date"),

        "user_status": payload.get("user_status", "Open"),
        "request_status": payload.get("request_status", "Pending"),

        "report_to": payload.get("report_to"),

        "active": payload.get("active", True),

        "created_at": datetime.now().isoformat()
    }

    request_collection.insert_one(record)

    # 🔥 remove ObjectId issue
    # record["_id"] = str(result.inserted_id)

    # Remove the ObjectId before returning it to the frontend
    del record["_id"] 

    return record