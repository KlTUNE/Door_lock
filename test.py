import RPi.GPIO as GPIO
import sys
import os
import atexit
import time

Senser = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Senser, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(Senser) == 0:
        print(0)
    else:
        print(1)
    time.sleep(1)
    print("-----------------")
