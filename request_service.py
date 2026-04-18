from data import requests_data
from datetime import datetime


def generate_request_no():

    return f"REQ{len(requests_data)+1:03d}"


def get_requests():

    return requests_data


def create_request(payload):

    new_request = {

        "request_no": generate_request_no(),

        "owner": payload.get("owner", "Karan"),

        "request_for": payload.get("request_for"),

        "subject": payload.get("subject"),

        "comments": payload.get("comments"),

        "open_date": payload.get("open_date"),

        "close_date": payload.get("close_date"),

        "actual_closed_date": payload.get("actual_closed_date"),

        "user_status": payload.get("user_status", "Open"),

        "request_status": payload.get("request_status", "Pending"),

        "report_to": payload.get("report_to"),

        "response_status": "Pending",

        "active": payload.get("active", True),

        "created_at": datetime.now().isoformat()

    }

    requests_data.append(new_request)

    return new_request