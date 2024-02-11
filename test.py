import RPi.GPIO as GPIO
import sys
import os
import atexit
import time

Senser = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Senser, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(Senser) :
        print(1)
    else:
        print(0)
