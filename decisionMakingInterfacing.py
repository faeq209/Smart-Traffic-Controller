import random
import time
import threading
from gpiozero import LED
from multiprocess_img import multi

# Initial Values
car_counts = {
    'lane1': 0,
    'lane2': 0,
    'lane3': 0,
    'lane4': 0,
}
counts_car = [0, 0, 0, 0]
ledPin1 = 17
ledPin2 = 22
ledPin3 = 27
ledPin4 = 14

led1 = LED(ledPin1)
led2 = LED(ledPin2)
led3 = LED(ledPin3)
led4 = LED(ledPin4)

def update_car_counts():
    global car_counts
    while True:
        new_car_counts = generate_random_car_counts()
        car_counts = new_car_counts
        sleep_duration = random.randint(10, 30)
        time.sleep(sleep_duration)

def switch(index):
    
    if index == '0':
        led1.on()
        led2.off()
        led3.off()
        led4.off()
    elif index == '1':
        led1.off()
        led2.on()
        led3.off()
        led4.off()
    elif index == '2':
        led1.off()
        led2.off()
        led3.on()
        led4.off()
    elif index == '3':
        led1.off()
        led2.off()
        led3.off()
        led4.on()
    else:
        led1.off()
        led2.off()
        led3.off()
        led4.off()

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
        time.sleep(duration)
        
        switch(index)

        index = (index + 1) % len(lanes_order)  # Move to the next lane in the order
        print(index)
        print(f"Number of threads: {threading.active_count()}")

# Calling the function
if __name__ == "__main__":
    car_count_thread = threading.Thread(target=update_car_counts)
    car_count_thread.start()

    traffic_controller()




## pin nos.  2 3 4 14