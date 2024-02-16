from modules import fp_ctl, lock_ctl
import RPi.GPIO as GPIO
import time

# 開錠ボタンの入力ピン番号
OPEN_PIN = 2
# 施錠ボタンの入力ピン番号
CLOSE_PIN = 3
# 指紋モジュールタッチセンサーの入力ピン番号
TOUCH_SENSOR_PIN = 4
# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OPEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CLOSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    # 最初に開錠しておく
    lock_ctl.open()
    # 開錠状態
    LOCK_STATUS = "OPEN"
    while True:
        try:
            # タッチセンサーが押されたら指紋認証を行う
            if GPIO.input(TOUCH_SENSOR_PIN) == 1:
                result = fp_ctl.search()
                if result and LOCK_STATUS == "LOCK":
                    lock_ctl.open()
                    LOCK_STATUS = "OPEN"
                elif LOCK_STATUS == "OPEN":
                    lock_ctl.lock()
                    LOCK_STATUS = "LOCK"
                # 指紋認証後、タッチセンサーが離されるまで待つ
                while GPIO.input(TOUCH_SENSOR_PIN) == 1: pass

            # 開錠ボタン、施錠ボタンが押されたら開錠、施錠を行う
            if GPIO.input(OPEN_PIN) == 0 and LOCK_STATUS == "LOCK":
                lock_ctl.open()
                LOCK_STATUS = "OPEN"
            if GPIO.input(CLOSE_PIN) == 0 and LOCK_STATUS == "OPEN":
                lock_ctl.lock()
                LOCK_STATUS = "LOCK"

        except KeyboardInterrupt:
            # Ctrl+Cが押されたらGIPを初期化して終了
            print("cleanup...")
            GPIO.cleanup()
            exit(1)
        # チャタリング防止のための待機
        time.sleep(0.2)

if __name__ == "__main__":
    main()