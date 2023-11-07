import random
import time
import threading
from gpiozero import LED
from multiprocess_img import multi
from db import push_traffic_data
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Initial Values
car_counts = {
    'lane1': 0,
    'lane2': 0,
    'lane3': 0,
    'lane4': 0,
}
counts_car = [0, 0, 0, 0]
Pin1g = 2
Pin1y = 3
Pin1r = 4

Pin2g = 17
Pin2y = 27
Pin2r = 22

Pin3g = 10
Pin3y = 9
Pin3r = 11

Pin4g = 5
Pin4y = 6
Pin4r = 13

GPIO.setup(Pin1r, GPIO.OUT)
GPIO.setup(Pin1y, GPIO.OUT)
GPIO.setup(Pin1g, GPIO.OUT)

GPIO.setup(Pin2r, GPIO.OUT)
GPIO.setup(Pin2y, GPIO.OUT)
GPIO.setup(Pin2g, GPIO.OUT)

GPIO.setup(Pin3r, GPIO.OUT)
GPIO.setup(Pin3y, GPIO.OUT)
GPIO.setup(Pin3g, GPIO.OUT)

GPIO.setup(Pin4r, GPIO.OUT)
GPIO.setup(Pin4y, GPIO.OUT)
GPIO.setup(Pin4g, GPIO.OUT)


def update_car_counts():
    global car_counts
    while True:
        new_car_counts = generate_random_car_counts()
        car_counts = new_car_counts
        sleep_duration = random.randint(10, 30)
        time.sleep(sleep_duration) 

def generate_random_car_counts():
    global counts_car
    counts_car=multi()
    car_counts = {}
    for lane in ['lane1', 'lane2', 'lane3', 'lane4']:
        car_counts[lane] = random.randint(0, 30)
    print(counts_car)
    return counts_car

def traffic_controller():
    lanes_order = ['lane1', 'lane2', 'lane3', 'lane4']
    index = 0
    
    while True:
        global car_counts, counts_car
        
        lane = lanes_order[index]
        print(counts_car)
        print(type(counts_car))
        max_car_count = counts_car[index]
        duration = min(30, round(10 + max_car_count*2/3)) 

        print(f"Opening {lane} for {duration} seconds")
        #switch(index, duration)
        #time.sleep(duration)
        
        #switch(index, duration)
        if index == 0:
            GPIO.output(Pin1g, GPIO.HIGH)
            GPIO.output(Pin2r, GPIO.HIGH)
            GPIO.output(Pin3r, GPIO.HIGH)
            GPIO.output(Pin4r, GPIO.HIGH)
            GPIO.output(Pin1y, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.LOW)
            GPIO.output(Pin1r, GPIO.LOW)
            GPIO.output(Pin2g, GPIO.LOW)
            GPIO.output(Pin3g, GPIO.LOW)
            GPIO.output(Pin4g, GPIO.LOW)
            push_traffic_data(counts_car[0], counts_car[1], counts_car[2], counts_car[3],1, 0,0, 0)
            time.sleep(duration)
            GPIO.output(Pin1g, GPIO.LOW)
            GPIO.output(Pin1y, GPIO.HIGH)
            time.sleep(5)
        elif index == 1:
            GPIO.output(Pin1g, GPIO.LOW)
            GPIO.output(Pin2r, GPIO.LOW)
            GPIO.output(Pin3r, GPIO.HIGH)
            GPIO.output(Pin4r, GPIO.HIGH)
            GPIO.output(Pin1y, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.LOW)
            GPIO.output(Pin1r, GPIO.HIGH)
            GPIO.output(Pin2g, GPIO.HIGH)
            GPIO.output(Pin3g, GPIO.LOW)
            GPIO.output(Pin4g, GPIO.LOW)
            push_traffic_data(counts_car[0], counts_car[1], counts_car[2], counts_car[3],0, 1,0, 0)
            time.sleep(duration)
            GPIO.output(Pin2g, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.HIGH)
            time.sleep(5)
        elif index == 2:
            GPIO.output(Pin1g, GPIO.LOW)
            GPIO.output(Pin2r, GPIO.HIGH)
            GPIO.output(Pin3r, GPIO.LOW)
            GPIO.output(Pin4r, GPIO.HIGH)
            GPIO.output(Pin1y, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.LOW)
            GPIO.output(Pin1r, GPIO.HIGH)
            GPIO.output(Pin2g, GPIO.LOW)
            GPIO.output(Pin3g, GPIO.HIGH)
            GPIO.output(Pin4g, GPIO.LOW)
            push_traffic_data(counts_car[0], counts_car[1], counts_car[2], counts_car[3],0, 0,1, 0)
            time.sleep(duration)
            GPIO.output(Pin3g, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.HIGH)
            time.sleep(5)
        elif index == 3:
            GPIO.output(Pin1g, GPIO.LOW)
            GPIO.output(Pin2r, GPIO.HIGH)
            GPIO.output(Pin3r, GPIO.HIGH)
            GPIO.output(Pin4r, GPIO.LOW)
            GPIO.output(Pin1y, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.LOW)
            GPIO.output(Pin1r, GPIO.HIGH)
            GPIO.output(Pin2g, GPIO.LOW)
            GPIO.output(Pin3g, GPIO.LOW)
            GPIO.output(Pin4g, GPIO.HIGH)
            push_traffic_data(counts_car[0], counts_car[1], counts_car[2], counts_car[3],0, 0,0, 1)
            time.sleep(duration)
            GPIO.output(Pin4g, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.HIGH)
            time.sleep(5)
        else:
            GPIO.output(Pin1g, GPIO.LOW)
            GPIO.output(Pin2r, GPIO.LOW)
            GPIO.output(Pin3r, GPIO.LOW)
            GPIO.output(Pin4r, GPIO.LOW)
            GPIO.output(Pin1y, GPIO.LOW)
            GPIO.output(Pin2y, GPIO.LOW)
            GPIO.output(Pin3y, GPIO.LOW)
            GPIO.output(Pin4y, GPIO.LOW)
            GPIO.output(Pin1r, GPIO.LOW)
            GPIO.output(Pin2g, GPIO.LOW)
            GPIO.output(Pin3g, GPIO.LOW)
            GPIO.output(Pin4g, GPIO.LOW)
            push_traffic_data(counts_car[0], counts_car[1], counts_car[2], counts_car[3],0, 0,0, 0)
            time.sleep(duration)


        index = (index + 1) % len(lanes_order)  # Move to the next lane in the order
        print(index)
        print(f"Number of threads: {threading.active_count()}")

# Calling the function
if __name__ == "__main__":
    car_count_thread = threading.Thread(target=update_car_counts)
    car_count_thread.start()

    traffic_controller()




## pin nos.  2 3 4 14
 
