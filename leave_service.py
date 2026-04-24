from db import db
from datetime import datetime

leave_collection = db["leaves"]


# ------------------
# GET LEAVES
# ------------------
def get_leaves():

    records = list(
        leave_collection.find({}, {"_id": 0})
    )

    return records


# ------------------
# CREATE LEAVE
# ------------------
def create_leave(payload):

    print("PAYLOAD:", payload)

    leave_type = payload.get("leaveType")
    from_date = payload.get("fromDate")
    to_date = payload.get("toDate")
    reason = payload.get("reason")


    # safety check
    if not from_date or not to_date:
        return {
            "success": False,
            "message": "Invalid dates"
        }


    # calculate days
    d1 = datetime.strptime(from_date, "%Y-%m-%d")
    d2 = datetime.strptime(to_date, "%Y-%m-%d")

    days = (d2 - d1).days + 1




    record = {
        "id": int(datetime.now().timestamp()),

        "leaveType": leave_type,
        "fromDate": from_date,
        "toDate": to_date,
        "days": days,
        "reason": reason,

        # default status
        "status": "Pending"
    }


    leave_collection.insert_one(record)
    
    # Remove the ObjectId before returning it to the frontend
    del record["_id"] 

    return record


def update_leave(id, payload):

    leave_type = payload.get("leaveType")
    from_date = payload.get("fromDate")
    to_date = payload.get("toDate")
    reason = payload.get("reason")

    d1 = datetime.strptime(from_date, "%Y-%m-%d")
    d2 = datetime.strptime(to_date, "%Y-%m-%d")

    days = (d2 - d1).days + 1

    updated = {
        "leaveType": leave_type,
        "fromDate": from_date,
        "toDate": to_date,
        "days": days,
        "reason": reason
    }

    # Remove the ObjectId before returning it to the frontend
    # del record["_id"] 
    # leave_collection.update_one(
    #     {"id": id},
    #     {"$set": updated}
    # )
    

    # return { "id": id, **updated }

    result = leave_collection.update_one(
        {"id": int(id)},
        {"$set": updated}
    )

    if result.matched_count == 0:
        return {"error": "Leave not found"}

    return {
        "id": int(id),
        **updated
    }


def delete_leave(id):

    result = leave_collection.delete_one({
        "id": int(id)
    })

    if result.deleted_count == 0:
        return {"error": "Leave not found"}

    return {"message": "deleted"}