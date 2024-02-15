import RPi.GPIO as GPIO
from modules import fp_ctl
import time

STATUS_LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(STATUS_LED_PIN, GPIO.OUT)

GPIO.output(STATUS_LED_PIN, 1)
while True:
    print("wait")
    time.sleep(1)