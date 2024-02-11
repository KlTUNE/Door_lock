import RPi.GPIO as GPIO
from modules import fp_ctl
import time

Senser = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Senser, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(Senser) == 1:
        fp_ctl.search()
        time.sleep(5)
    # time.sleep(1)
    print(GPIO.input(Senser))