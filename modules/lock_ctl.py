import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
STATUS_LED_PIN = 17

def _init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(STATUS_LED_PIN, GPIO.OUT)
    servo = GPIO.PWM(SERVO_PIN, 50)
    servo.start(0)
    return servo

def open():
    servo = _init()
    GPIO.output(STATUS_LED_PIN, 0)
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()


def lock():
    servo = _init()
    GPIO.output(STATUS_LED_PIN, 1)
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    open()
    time.sleep(5)
    lock()
    pass
