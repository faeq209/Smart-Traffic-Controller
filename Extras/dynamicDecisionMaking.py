import random
import time
import threading

# Initial Values
car_counts = {
    'lane1': 0,
    'lane2': 0,
    'lane3': 0,
    'lane4': 0,
}

def update_car_counts():
    global car_counts
    while True:

        new_car_counts = generate_random_car_counts()
        car_counts = new_car_counts

        sleep_duration = random.randint(10, 30)
        time.sleep(sleep_duration)

def open_lane(lane, duration):
    print(f"Opening {lane} for {duration} seconds")

def determine_next_lane(car_counts):
    max_lane = max(car_counts, key=car_counts.get)
    return max_lane

def generate_random_car_counts():
    car_counts = {}
    for lane in ['lane1', 'lane2', 'lane3', 'lane4']:
        car_counts[lane] = random.randint(0, 30)
    return car_counts

def traffic_controller():
    while True:
        global car_counts
        
        next_lane = determine_next_lane(car_counts)
        print(car_counts)
        print(next_lane)

        max_car_count = max(car_counts.values())
        duration = min(30, round(10 + max_car_count*2/3)) 

        open_lane(next_lane, duration)
        time.sleep(duration)

# Calling the function
if __name__ == "__main__":
    car_count_thread = threading.Thread(target=update_car_counts)
    car_count_thread.start()

    traffic_controller()
