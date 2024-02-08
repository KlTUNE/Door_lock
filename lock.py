import RPi.GPIO as GPIO
import time
import os

servo_pin = 14
LED_pin = 23
lock_status_old = "null"

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(LED_pin, GPIO.OUT)

status_LED = GPIO.PWM(LED_pin, 50)
servo = GPIO.PWM(servo_pin, 50)
servo.start(0)
status_LED.start(0)

status = open('./lock.status', 'w')
status.write('=close')
status.close()

time.sleep(20)
os.system("sudo tmux new -s button -d 'sudo python button.py'")

print ("start lock")

while True:
    status = open('./lock.status', 'r')
    lock_status = status.read()
    status.close()

    if lock_status_old != lock_status:
        lock_status_old = lock_status
        os.system("sudo tmux kill-session -t key")

        if lock_status == "=open":
            print("open_OK")
            status_LED.ChangeDutyCycle(0)
            servo.ChangeDutyCycle(7.25)
            time.sleep(0.5)
            servo.ChangeDutyCycle(0)

        elif lock_status == "=close":
            print("close_OK")
            status_LED.ChangeDutyCycle(30)
            servo.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            servo.ChangeDutyCycle(0)

        elif lock_status == "open-close":
            print("open-close_OK")
            status_LED.ChangeDutyCycle(0)
            servo.ChangeDutyCycle(7.25)
            time.sleep(0.5)
            servo.ChangeDutyCycle(0)
            time.sleep(5)
            status_LED.ChangeDutyCycle(30)
            servo.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            servo.ChangeDutyCycle(0)
            status = open('./lock.status', 'w')
            status.write('=close')
            status.close()
            lock_status_old = "=close"

        print  ("restart key.py")
        os.system("sudo tmux new -s key -d 'sudo python key.py'")