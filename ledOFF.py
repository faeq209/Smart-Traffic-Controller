import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
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
