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
servo.start(0)


#角度からデューティ比を求め、サーボを動かす
def servo_angle(angle):
    #角度からデューティ比を求める
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

# 開錠
def open():
    print("OPEN")
    # ステータスLEDを消灯
    GPIO.output(STATUS_LED_PIN, 0)
    servo_angle(10)

# 施錠
def lock():
    print("LOCK")
    # ステータスLEDを点灯
    GPIO.output(STATUS_LED_PIN, 1)
    servo_angle(-90)


# エラー時のLED点滅
def error_led():
    for _ in range(3):
        GPIO.output(STATUS_LED_PIN, 1)
        time.sleep(0.1)
        GPIO.output(STATUS_LED_PIN, 0)
        time.sleep(0.1)
    GPIO.output(STATUS_LED_PIN, 1)

# ステータスLEDの点灯
def led_on():
    GPIO.output(STATUS_LED_PIN, 1)
# ステータスLEDの消灯
def led_off():
    GPIO.output(STATUS_LED_PIN, 0)

# GPIOの初期化
def cleanup():
    print("CLEANUP...")
    GPIO.cleanup()
    servo.stop()

if __name__ == "__main__":
    try:
        OPEN_PIN = 2
        CLOSE_PIN = 3
        GPIO.setup(OPEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(CLOSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            if GPIO.input(OPEN_PIN) == 0: open()
            if GPIO.input(CLOSE_PIN) == 0: lock()
            time.sleep(0.1)
    except KeyboardInterrupt: cleanup()
