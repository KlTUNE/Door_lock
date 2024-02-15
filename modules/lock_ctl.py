import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
STATUS_LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(STATUS_LED_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

def open():
    print('open')
    GPIO.output(STATUS_LED_PIN, 0)
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def lock():
    print('lock')
    GPIO.output(STATUS_LED_PIN, 1)
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def cleanup():
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    open()
    time.sleep(5)
    lock()
    pass
