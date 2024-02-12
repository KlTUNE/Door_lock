import RPi.GPIO as GPIO
from modules import fp_ctl
import time

TOUCH_SENSOR_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(TOUCH_SENSOR_PIN) == 1:
        fp_ctl.search()
        time.sleep(5)