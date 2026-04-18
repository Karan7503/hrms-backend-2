from flask import Flask, request, jsonify
from flask_cors import CORS

from attendance_service import get_attendance_data

from request_service import get_requests, create_request

from seed_requests import seed_requests


app = Flask(__name__)

CORS(app)


# ------------------
# attendance api
# ------------------

@app.route("/attendance", methods=["GET"])
def attendance():

    records, summary = get_attendance_data()

    return jsonify({
        "records": records,
        "summary": summary
    })


# ------------------
# requests api
# ------------------

@app.route("/requests", methods=["GET"])
def fetch_requests():

    return {
        "records": get_requests()
    }



@app.route("/requests", methods=["POST"])
def add_request():

    payload = request.json

    new_request = create_request(payload)

    return {
        "message": "created",
        "record": new_request
    }



# ------------------

if __name__ == "__main__":

    seed_requests()

    app.run(debug=True, use_reloader=False)