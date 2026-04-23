from flask import Flask, request, jsonify
from flask_cors import CORS

from attendance_service import get_attendance_data

from request_service import get_requests, create_request

from seed_requests import seed_requests

from conference_service import get_slots, create_booking

from leave_service import get_leaves, create_leave

app = Flask(__name__)

CORS(app)


# ------------------
# attendance api
# ------------------

@app.route("/attendance", methods=["GET"])
def attendance():

    # records, summary 
    start = request.args.get("start")
    end = request.args.get("end")

    print("API PARAMS:", start, end)

    records, summary = get_attendance_data(start, end)


    return jsonify({
        "records": records,
        "summary": summary
    })


# ------------------
# requests api
# ------------------

# @app.route("/requests", methods=["GET"])
# def fetch_requests():

#     return {
#         "records": get_requests()
#     }



# @app.route("/requests", methods=["POST"])
# def add_request():

#     payload = request.json

#     new_request = create_request(payload)

#     return {
#         "message": "created",
#         "record": new_request
#     }


@app.route("/requests", methods=["GET"])
def fetch_requests():
    return jsonify({
        "records": get_requests()
    })


@app.route("/requests", methods=["POST"])
def add_request():
    payload = request.json

    record = create_request(payload)

    return jsonify({
        "message": "created",
        "record": record
    })

# ------------------
# conference api
# ------------------

@app.route("/conference/slots", methods=["GET"])
def conference_slots():

    room = request.args.get("room")
    date = request.args.get("date")

    slots = get_slots(room, date)

    return {

        "records": slots
    }


@app.route("/conference/book", methods=["POST"])
def conference_book():

    payload = request.json

    result = create_booking(payload)


    if result["success"] == False:

        return jsonify(result), 400


    return jsonify(result)


# ------------------
# leave api
# ------------------

@app.route("/leave", methods=["GET"])
def fetch_leave():

    records = get_leaves()

    return jsonify({
        "records": records
    })


@app.route("/leave", methods=["POST"])
def add_leave():

    payload = request.json

    record = create_leave(payload)

    return jsonify({
        "message": "created",
        "record": record
    })



# ------------------

if __name__ == "__main__":

    seed_requests()

    app.run(debug=True, use_reloader=False)