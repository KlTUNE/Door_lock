import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
STATUS_LED_PIN = 17
servo = None

def _init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(STATUS_LED_PIN, GPIO.OUT)
    servo = GPIO.PWM(SERVO_PIN, 50)
    servo.start(0)

def _clean():
    servo.stop()
    GPIO.cleanup()

def open():
    _init()
    GPIO.output(STATUS_LED_PIN, 0)
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    _clean()


def lock():
    _init()
    GPIO.output(STATUS_LED_PIN, 1)
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    _clean()

if __name__ == "__main__":
    # open()
    # lock()
    pass
