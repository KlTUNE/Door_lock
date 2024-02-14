from modules import fp_ctl, lock_ctl
import RPi.GPIO as GPIO

OPEN_PIN = 2
CLOSE_PIN = 3
TOUCH_SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(OPEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CLOSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    while True:
        if GPIO.input(TOUCH_SENSOR_PIN) == 1:
            result = fp_ctl.search()
            if result: lock_ctl.open()
            else: lock_ctl.lock()

        if GPIO.input(OPEN_PIN) == 0:
            lock_ctl.open()

        if GPIO.input(CLOSE_PIN) == 0:
            lock_ctl.lock()

if __name__ == "__main__":
    try:
        lock_ctl.open()
        main()
    except:
        print("clean")
        GPIO.cleanup()