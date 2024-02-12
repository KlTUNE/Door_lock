from modules import fp_ctl, lock_ctl
import os, time
import RPi.GPIO as GPIO
import datetime
import os

OPEN_PIN = 3
CLOSE_PIN = 4
TOUCH_SENSOR_PIN = 14
open_button = 15
close_button = 17
lock_status = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(OPEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(close_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# os.system("sudo tmux new -s key -d 'sudo python key.py'")

def main():
    while True:
        pass


if __name__ == "__main__":
    main()
    pass