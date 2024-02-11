import RPi.GPIO as GPIO
from modules import fp_ctl
import time

Senser = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Senser, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(Senser) == 0:
        fp_ctl.search()
    # time.sleep(1)