from datetime import datetime, timedelta
from db import attendance_collection


def daterange(start_date, end_date):

    for n in range((end_date - start_date).days + 1):
        yield start_date + timedelta(n)



def is_weekoff(date_obj):

    weekday = date_obj.strftime("%A")

    # Sunday always week off
    if weekday == "Sunday":
        return True

    # Saturday logic
    if weekday == "Saturday":

        # which saturday of the month?
        saturday_number = (date_obj.day - 1) // 7 + 1

        # 2nd, 4th, 6th saturday -> week off
        if saturday_number in [2, 4, 6]:
            return True

    return False



def get_attendance_data(start=None, end=None):

    if not start or not end:

        today = datetime.today()

        start_date = today.replace(day=1)

        if today.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=today.month + 1, day=1)

        end_date = next_month - timedelta(days=1)

    else:

        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")


    query = {
        "date": {
            "$gte": start_date.strftime("%Y-%m-%d"),
            "$lte": end_date.strftime("%Y-%m-%d")
        }
    }

    db_records = list(
        attendance_collection.find(query, {"_id": 0})
    )


    db_map = {
        r["date"]: r
        for r in db_records
    }


    records = []


    for date_obj in daterange(start_date, end_date):

        date_str = date_obj.strftime("%Y-%m-%d")

        # 1️⃣ check DB attendance (Present, Late, Absent only)
        if date_str in db_map and db_map[date_str]["status"] not in ["Holiday"]:

            records.append(db_map[date_str])

            continue


        # 2️⃣ apply weekoff logic
        if is_weekoff(date_obj):

            records.append({

                "date": date_str,
                "status": "Weekly Off",
                "inTime": "-",
                "outTime": "-",
                "hours": 0

            })

            continue


        # 3️⃣ fallback to DB holiday (future admin holiday list)
        if date_str in db_map and db_map[date_str]["status"] == "Holiday":

            records.append(db_map[date_str])

            continue


        # 4️⃣ working day without entry
        records.append({

            "date": date_str,
            "status": "",
            "inTime": "-",
            "outTime": "-",
            "hours": 0

        })


    # summary
    total_days = len(records)

    present = sum(1 for r in records if r["status"] == "Present")
    absent = sum(1 for r in records if r["status"] == "Absent")
    late = sum(1 for r in records if r["status"] == "Late")
    holiday = sum(1 for r in records if r["status"] == "Holiday")
    weekoff = sum(1 for r in records if r["status"] == "Weekly Off")


    working_days = total_days - holiday - weekoff


    attendance_percent = 0

    if working_days > 0:

        attendance_percent = round(
            (present / working_days) * 100
        )


    summary = {

        "totalDays": total_days,
        "present": present,
        "absent": absent,
        "late": late,
        "holiday": holiday,
        "weekOff": weekoff,
        "attendancePercent": attendance_percent

    }


    return records, summary