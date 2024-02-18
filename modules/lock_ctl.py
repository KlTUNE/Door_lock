import RPi.GPIO as GPIO
from modules import record_log
import time

# サーボのPWMの出力ピン番号
SERVO_PIN = 18
# ステータスLEDの出力ピン番号
STATUS_LED_PIN = 17
# GIPOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(STATUS_LED_PIN, GPIO.OUT)
# サーボのPWMの設定
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

# 開錠
def open():
    print(" | ".join(record_log.read_before_log()))
    # ステータスLEDを消灯
    GPIO.output(STATUS_LED_PIN, 0)
    # サーボを左に90度回転
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.8)
    servo.ChangeDutyCycle(0)

# 施錠
def lock():
    print(" | ".join(record_log.read_before_log()))
    # ステータスLEDを点灯
    GPIO.output(STATUS_LED_PIN, 1)
    # サーボを右に90度回転
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.8)
    servo.ChangeDutyCycle(0)

# エラー時のLED点滅
def error_led():
    for _ in range(3):
        GPIO.output(STATUS_LED_PIN, 1)
        time.sleep(0.1)
        GPIO.output(STATUS_LED_PIN, 0)
        time.sleep(0.1)
    GPIO.output(STATUS_LED_PIN, 1)

# GPIOの初期化
def cleanup():
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    open()
    time.sleep(5)
    lock()
    pass
