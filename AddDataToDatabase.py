import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendencerealtime-c594f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12112167":
        {
            "name": "Parnoor",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12112174":
        {
            "name": "Lovepreet",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12112168":
        {
            "name": "Tanu",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)

