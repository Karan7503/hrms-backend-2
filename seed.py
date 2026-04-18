from db import attendance_collection

# optional: clear previous data
attendance_collection.delete_many({})

data = [

# APRIL 2026
{"date":"2026-04-01","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-02","status":"Present","inTime":"09:10","outTime":"18:05","hours":8.9},
{"date":"2026-04-03","status":"Late","inTime":"09:45","outTime":"18:00","hours":8},
{"date":"2026-04-04","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-05","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-06","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-07","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-04-08","status":"Late","inTime":"09:35","outTime":"18:00","hours":8.3},
{"date":"2026-04-09","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-10","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-11","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-12","status":"Present","inTime":"09:00","outTime":"18:10","hours":9.1},
{"date":"2026-04-13","status":"Late","inTime":"09:50","outTime":"18:00","hours":8},
{"date":"2026-04-14","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-15","status":"Present","inTime":"09:15","outTime":"18:05","hours":8.8},
{"date":"2026-04-16","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-17","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-18","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-19","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-04-20","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-21","status":"Late","inTime":"09:40","outTime":"18:00","hours":8.2},
{"date":"2026-04-22","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-23","status":"Present","inTime":"09:00","outTime":"18:10","hours":9.1},
{"date":"2026-04-24","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-25","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-04-26","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-27","status":"Present","inTime":"09:10","outTime":"18:00","hours":8.8},
{"date":"2026-04-28","status":"Late","inTime":"09:55","outTime":"18:00","hours":8},
{"date":"2026-04-29","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-04-30","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},

# MAY 2026
{"date":"2026-05-01","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-02","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-03","status":"Present","inTime":"09:00","outTime":"18:05","hours":9},
{"date":"2026-05-04","status":"Late","inTime":"09:35","outTime":"18:00","hours":8.3},
{"date":"2026-05-05","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-06","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-07","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-05-08","status":"Late","inTime":"09:40","outTime":"18:00","hours":8.2},
{"date":"2026-05-09","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-10","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-11","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-12","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-13","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-14","status":"Late","inTime":"09:45","outTime":"18:00","hours":8},
{"date":"2026-05-15","status":"Present","inTime":"09:00","outTime":"18:05","hours":9},
{"date":"2026-05-16","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-17","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-18","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-05-19","status":"Late","inTime":"09:50","outTime":"18:00","hours":8},
{"date":"2026-05-20","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},

# MAY 2026
{"date":"2026-05-01","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-02","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-03","status":"Present","inTime":"09:00","outTime":"18:05","hours":9},
{"date":"2026-05-04","status":"Late","inTime":"09:35","outTime":"18:00","hours":8.3},
{"date":"2026-05-05","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-06","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-07","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-05-08","status":"Late","inTime":"09:40","outTime":"18:00","hours":8.2},
{"date":"2026-05-09","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-10","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-11","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-12","status":"Absent","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-13","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-14","status":"Late","inTime":"09:45","outTime":"18:00","hours":8},
{"date":"2026-05-15","status":"Present","inTime":"09:00","outTime":"18:05","hours":9},
{"date":"2026-05-16","status":"Holiday","inTime":"-","outTime":"-","hours":0},
{"date":"2026-05-17","status":"Present","inTime":"09:00","outTime":"18:00","hours":9},
{"date":"2026-05-18","status":"Present","inTime":"09:05","outTime":"18:00","hours":8.9},
{"date":"2026-05-19","status":"Late","inTime":"09:50","outTime":"18:00","hours":8},
{"date":"2026-05-20","status":"Present","inTime":"09:00","outTime":"18:00","hours":9}

]

attendance_collection.insert_many(data)

print("Dummy attendance inserted:", len(data))