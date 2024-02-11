# import RPi.GPIO as GPIO
# import time

# servo_pin = 14
# LED_pin = 23
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servo_pin, GPIO.OUT)
# GPIO.setup(LED_pin, GPIO.OUT)
# status_LED = GPIO.PWM(LED_pin, 50)
# status_LED.start(0)
# servo = GPIO.PWM(servo_pin, 50)
# servo.start(0)

# def open():
#     print("open")
#     status_LED.ChangeDutyCycle(0)
#     servo.ChangeDutyCycle(7.25)
#     time.sleep(0.5)
#     servo.ChangeDutyCycle(0)

# def lock():
#     print("lock")
#     status_LED.ChangeDutyCycle(30)
#     servo.ChangeDutyCycle(2.5)
#     time.sleep(0.5)
#     servo.ChangeDutyCycle(0)

# if __name__ == '__main__':
#     # open()
#     # lock()
#     pass