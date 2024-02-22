import RPi.GPIO as GPIO
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

#角度からデューティ比を求め、サーボを動かす
def servo_angle(angle):
    #角度からデューティ比を求める
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    # duty = 3 + (19 / 36) * angle
    servo.start(0)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo.stop()

# 開錠
def open():
    print("OPEN")
    # ステータスLEDを消灯
    GPIO.output(STATUS_LED_PIN, 0)
    servo_angle(90)
    # servo.ChangeDutyCycle(7.25)
    # time.sleep(0.5)
    # servo.ChangeDutyCycle(0)

# 施錠
def lock():
    print("LOCK")
    # ステータスLEDを点灯
    GPIO.output(STATUS_LED_PIN, 1)
    servo_angle(0)
    # servo.ChangeDutyCycle(2.5)
    # time.sleep(0.5)
    # servo.ChangeDutyCycle(0)

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
    GPIO.cleanup()

if __name__ == "__main__":
    open()
    time.sleep(5)
    lock()
    pass
