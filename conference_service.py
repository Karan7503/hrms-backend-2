from db import conference_collection
from datetime import datetime

TIME_SLOTS = [

    "08:00 AM",
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",

    "12:00 PM",
    "01:00 PM",
    "02:00 PM",
    "03:00 PM",

    "04:00 PM",
    "05:00 PM",
    "06:00 PM",

    "07:00 PM",
    "08:00 PM",
    "09:00 PM"
]


def get_slots(room, date):

    bookings = list(
        conference_collection.find(
            {
                "room": room,
                "date": date
            },
            {"_id": 0}
        )
    )


    booked_map = {

        b["start_time"]: b

        for b in bookings

    }


    slots = []


    for t in TIME_SLOTS:

        if t in booked_map:

            slots.append({

                "time": t,
                "title": booked_map[t]["title"],
                "status": "booked"

            })

        else:

            slots.append({

                "time": t,
                "title": "",
                "status": "available"

            })


    return slots


# check if slot is in past
def is_past_time(date_str, start_time):

    now = datetime.now()

    booking_datetime = datetime.strptime(
        f"{date_str} {start_time}",
        "%Y-%m-%d %I:%M %p"
    )

    return booking_datetime < now



# create booking
def create_booking(payload):

    room = payload.get("room")
    date = payload.get("date")

    start_time = payload.get("start_time")
    end_time = payload.get("end_time")

    subject = payload.get("subject")


    # 1️⃣ prevent booking past time
    if is_past_time(date, start_time):

        return {

            "success": False,
            "message": "Cannot book past time slot"

        }


    # 2️⃣ prevent double booking
    existing = conference_collection.find_one({

        "room": room,
        "date": date,
        "start_time": start_time

    })


    if existing:

        return {

            "success": False,
            "message": "Slot already booked"

        }


    # 3️⃣ create booking
    record = {

        "room": room,
        "date": date,

        "start_time": start_time,
        "end_time": end_time,

        "title": subject,

        "status": "booked"
    }


    result = conference_collection.insert_one(record)

    record["_id"] = str(result.inserted_id)


    return {

        "success": True,
        "record": record

    }