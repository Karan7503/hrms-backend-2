from db import attendance_collection


def get_attendance_data(start=None, end=None):

    query = {}

    # filter by date
    if start and end:
        query["date"] = {
            "$gte": start,
            "$lte": end
        }

    records = list(attendance_collection.find(query, {"_id": 0}))

    # summary calculation
    total_days = len(records)

    present = sum(1 for r in records if r["status"] == "Present")
    absent = sum(1 for r in records if r["status"] == "Absent")
    late = sum(1 for r in records if r["status"] == "Late")
    holiday = sum(1 for r in records if r["status"] == "Holiday")

    attendance_percent = 0

    if total_days > 0:
        attendance_percent = round((present / total_days) * 100)

    summary = {
        "totalDays": total_days,
        "present": present,
        "absent": absent,
        "late": late,
        "holiday": holiday,
        "attendancePercent": attendance_percent
    }

    return records, summary