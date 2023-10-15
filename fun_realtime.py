import pyrebase


def initialize_firebase():
    config = {"apiKey": "AIzaSyB6QDtvyQclAqjIA4z8x5CuTn9H_I2Y_9E",
              "authDomain": "traffic-light-controller-ab5c2.firebaseapp.com",
              "databaseURL": "https://traffic-light-controller-ab5c2-default-rtdb.firebaseio.com",
              "projectId": "traffic-light-controller-ab5c2",
              "storageBucket": "traffic-light-controller-ab5c2.appspot.com",
              "messagingSenderId": "232091657076",
              "appId": "1:232091657076:web:be63310b464f7841744221",
              "measurementId": "G-J3G3BL5V15"
              }
    firebase = pyrebase.initialize_app(config)
    return firebase.database()


def push_traffic_data(database, vehicles_1, vehicles_2, vehicles_3, vehicles_4,light_1, light_2,
                      light_3, light_4):
    db = initialize_firebase()
    data = {
        "lane_1": {
            "total_vehicles": vehicles_1,
            "traffic_light": light_1  # 1 for green
        },
        "lane_2": {
            "total_vehicles": vehicles_2,
            "traffic_light": light_2  # 0 for red
        },
        "lane_3": {
            "total_vehicles": vehicles_3,
            "traffic_light": light_3  # 0 for red
        },
        "lane_4": {
            "total_vehicles": vehicles_4,
            "traffic_light": light_4  # 0 for red
        }
    }
    database.child('traffic_data').set(data)


if __name__ == "__main__":
    # Initialize Firebase


    # Define your traffic data
    lane_1_vehicles = 50
    lane_2_vehicles = 80
    lane_3_vehicles = 160
    lane_4_vehicles = 70

    # Define traffic lights
    trafficlight_1 = 1
    trafficlight_2 = 1
    trafficlight_3 = 0
    trafficlight_4 = 0

    # Push traffic data to the Firebase database
    push_traffic_data(db, lane_1_vehicles, lane_2_vehicles, lane_3_vehicles, lane_4_vehicles, trafficlight_1, trafficlight_2, trafficlight_3,
                      trafficlight_4)
