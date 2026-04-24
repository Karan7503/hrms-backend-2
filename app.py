from flask import Flask, request, jsonify
from flask_cors import CORS

from auth_service import authenticate_user, seed_demo_users

from attendance_service import get_attendance_data

from request_service import get_requests, create_request, update_request, delete_request

from seed_requests import seed_requests

from conference_service import get_slots, create_booking

from leave_service import get_leaves, create_leave, update_leave, delete_leave

app = Flask(__name__)

CORS(app)







# ------------------
# auth api
# ------------------

@app.route("/login", methods=["POST"])
def login():
    payload = request.json
    email = payload.get("email")
    password = payload.get("password")
    
    result = authenticate_user(email, password)
    
    if result["success"]:
        return jsonify(result)
    else:
        return jsonify(result), 401





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



@app.route("/requests/<id>", methods=["PUT"])
def edit_request(id):

    id = int(id)
    print("EDIT REQUEST HIT:", id)

    payload = request.json

    record = update_request(id, payload)

    return jsonify({
        "message": "updated",
        "record": record
    })


@app.route("/requests/<id>", methods=["DELETE"])
def remove_request(id):

    print("DELETE REQUEST HIT:", id)

    result = delete_request(id)

    return jsonify(result)








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

@app.route("/leave/<id>", methods=["PUT"])
def edit_leave(id):

    id = int(id)
    print("EDIT API HIT:", id)
    payload = request.json

    record = update_leave(id, payload)

    return jsonify({
        "message": "updated",
        "record": record
    })
    

@app.route("/leave/<id>", methods=["DELETE"])
def remove_leave(id):

    print("DELETE LEAVE HIT:", id)

    result = delete_leave(id)

    return jsonify(result)

# ------------------

if __name__ == "__main__":

    # seed_requests()
    seed_demo_users()

    app.run(debug=True, use_reloader=False)