import RPi.GPIO as GPIO
import datetime
import os

open_button = 15
close_button = 18
lock_status = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(open_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(close_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print ("start button")
os.system("sudo tmux new -s key -d 'sudo python key.py'")

while True:
    status = open('./lock.status', 'r')
    lock_status = status.read()
    status.close()

    now_time = datetime.datetime.now()

    if now_time.hour == 1 and now_time.minute == 0 and now_time.second < 2 and lock_status != "=open":
        print("time_open")
        status = open('./lock.status', 'w')
        status.write('=open')
        status.close()

    elif GPIO.input(open_button) == 0 and lock_status != "=open":
        print("button_open")
        status = open('./lock.status', 'w')
        status.write('=open')
        status.close()

    elif GPIO.input(close_button) == 0 and lock_status != "=close":
        print("button_close")
        status = open('./lock.status', 'w')
        status.write('=close')
        status.close()

    lock_status_old = lock_status