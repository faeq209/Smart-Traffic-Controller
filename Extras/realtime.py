import pyrebase

config = {"apiKey": "AIzaSyB6QDtvyQclAqjIA4z8x5CuTn9H_I2Y_9E",
          "authDomain": "traffic-light-controller-ab5c2.firebaseapp.com",
          "databaseURL": "https://traffic-light-controller-ab5c2-default-rtdb.firebaseio.com",
          "projectId": "traffic-light-controller-ab5c2",
          "storageBucket": "traffic-light-controller-ab5c2.appspot.com",
          "messagingSenderId": "232091657076",
          "appId": "1:232091657076:web:be63310b464f7841744221",
          "measurementId": "G-J3G3BL5V15"
          }
# initialize the app
firebase = pyrebase.initialize_app(config)
# connect to database
database = firebase.database()
# push data(real time stamp)
cnt1=97
data = {
    "lane_1": {
        "total_vehicles": cnt1,
        "traffic_light": 1  # 0 for red, 1 for green
    },
    "lane_2": {
        "total_vehicles": 80,
        "traffic_light": 0  # 0 for red, 1 for green
    },
    "lane_3": {
        "total_vehicles": 160,
        "traffic_light": 0  # 0 for red, 1 for green
    },
    "lane_4": {
        "total_vehicles": 70,
        "traffic_light": 0  # 0 for red, 1 for green
    }
}
database.child('traffic_data').set(data)  # set method is used to change value inside same key
# push method is used to generate a new id each time
