from modules import fp_ctl, lock_ctl, record_log
import RPi.GPIO as GPIO
import time, datetime
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
    # 自動開錠する時刻の設定
    OPEN_TIME = [2, 0, 0]
    open_time = datetime.time(OPEN_TIME[0], OPEN_TIME[1], OPEN_TIME[2])
    diff_open_time = datetime.time(OPEN_TIME[0], OPEN_TIME[1], OPEN_TIME[2] + 1)
    # 最初に開錠しておく
    lock_ctl.lock()
    lock_ctl.open()
    record_log.write_log("BOOT", "OPEN", "SUCCESS")
    while True:
        # タッチセンサーが押されたら指紋認証を行う
        if GPIO.input(TOUCH_SENSOR_PIN) == 1:
            result = fp_ctl.search()
            # 右人差し指が検出された場合、開錠する
            if result == 0 or result == 1:
                lock_ctl.open()
                record_log.write_log(f"FINGER[#{result}]", "OPEN", "SUCCESS")
            # 右親指が検出された場合、施錠する
            elif result == 2:
                if record_log.read_before_log()[2] != "LOCK": lock_ctl.lock()
                record_log.write_log(f"FINGER[#{result}]", "LOCK", "SUCCESS")
            # 指紋が登録されていない場合、施錠し、エラーを記録する
            elif result == -1:
                if record_log.read_before_log()[2] != "LOCK": lock_ctl.lock()
                record_log.write_log(f"FINGER[#{result}]", "ERROR", "FINGER ERROR")
                lock_ctl.error_led()
            # 指紋認証後、タッチセンサーが押されていた場合、指が離されるまで待つ
            while GPIO.input(TOUCH_SENSOR_PIN) == 1: pass

        # 開錠ボタン、施錠ボタンが押されたら開錠、施錠を行う
        if GPIO.input(OPEN_PIN) == 0:
            lock_ctl.open()
            record_log.write_log("BUTTON", "OPEN", "SUCCESS")
        if GPIO.input(CLOSE_PIN) == 0:
            if record_log.read_before_log()[2] != "LOCK": lock_ctl.lock()
            record_log.write_log("BUTTON", "LOCK", "SUCCESS")

        # 自動開錠する時刻になったら開錠する
        dt_now = datetime.datetime.now()
        if dt_now.time() > open_time and dt_now.time() < diff_open_time:
            lock_ctl.open()
            record_log.write_log("TIME", "OPEN", "SUCCESS")
            time.sleep(1)

        # チャタリング防止のための待機
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+Cが押されたらGIPを初期化して終了
        lock_ctl.open()
        print("cleanup...")
        GPIO.cleanup()
        exit(1)