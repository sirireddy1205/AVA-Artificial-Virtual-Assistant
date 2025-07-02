import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C:\\Users\\sirignya reddy\\PycharmProjects\\FaceAttendance\\.venv\\serviceAccountKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-c58d2-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')
data = {
    "1":
        {
            "name": " Siri ",
            "major": " IT ",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "2":
        {
            "name": " Musk ",
            "major": " Fashion ",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "3":
        {
            "name": " Pawan ",
            "major": " Literature ",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)