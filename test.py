import RPi.GPIO as GPIO
import sys
import os
import atexit
import time

# TouchSenser

Senser = 24

def senser_callback(gpio_pin):
    # ピンの値を出力
    print(GPIO.input(Senser))

def end():
    # GPIOの開放
    GPIO.cleanup()

def standby():
    # GPIO初期化
    GPIO.setmode(GPIO.BCM)
    # 内部プルアップ設定
    GPIO.setup(Senser, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # 割り込み背動作設定とチャリング対策
    GPIO.add_event_detect(Senser, GPIO.BOTH, bouncetime=50)
    # コールバック指
    GPIO.add_event_callback(Senser, senser_callback)
    # 終了時指定
    atexit.register(end)
    # 無限ループ

    while True:
        time.sleep(60)

if __name__ == "__main__":
    standby()
