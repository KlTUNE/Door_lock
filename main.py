from modules import fp_ctl, record_log
import RPi.GPIO as GPIO
import time, datetime

# 開錠ボタンの入力ピン番号
OPEN_PIN = 2
# 施錠ボタンの入力ピン番号
CLOSE_PIN = 3
# 指紋モジュールタッチセンサーの入力ピン番号
TOUCH_SENSOR_PIN = 4
# サーボのPWMの出力ピン番号
SERVO_PIN = 18
# ステータスLEDの出力ピン番号
STATUS_LED_PIN = 17
# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OPEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CLOSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

# 開錠
def open():
    # ステータスLEDを消灯
    GPIO.output(STATUS_LED_PIN, 0)
    servo_angle(20)

# 施錠
def lock():
    # ステータスLEDを点灯
    GPIO.output(STATUS_LED_PIN, 1)
    servo_angle(-70)


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

def main():
    # 自動開錠する時刻の設定
    OPEN_TIME = [2, 0, 0]
    open_time = datetime.time(OPEN_TIME[0], OPEN_TIME[1], OPEN_TIME[2])
    diff_open_time = datetime.time(OPEN_TIME[0], OPEN_TIME[1], OPEN_TIME[2] + 1)
    # 最初に開錠しておく
    lock()
    open()
    # 指紋認証モジュールの初期化
    fp_module = fp_ctl.init_fp_module()
    record_log.write_log("BOOT", "OPEN", "SUCCESS")
    while True:
        result = fp_ctl.search(fp_module)
        if result != 999:
            print("指紋が検出されました")
            # 右人差し指が検出された場合、開錠する
            if result == 0 or result == 1:
                open()
                record_log.write_log(f"FINGER[#{result}]", "OPEN", "SUCCESS")
            # 右親指が検出された場合、施錠する
            elif result == 2:
                if record_log.read_before_log()[2] != "LOCK": lock()
                record_log.write_log(f"FINGER[#{result}]", "LOCK", "SUCCESS")
            # 指紋が登録されていない場合、施錠し、エラーを記録する
            elif result == -1:
                if record_log.read_before_log()[2] != "LOCK": lock()
                record_log.write_log(f"FINGER[#{result}]", "ERROR", "FINGER ERROR")
                error_led()


            # 指紋認証モジュールから手が離されるまで待機
            while fp_ctl.search(fp_module) != 999:
                print("指を離してください")
                pass
            print("離されました")

        # 開錠ボタン、施錠ボタンが押されたら開錠、施錠を行う
        if GPIO.input(OPEN_PIN) == 0:
            open()
            record_log.write_log("BUTTON", "OPEN", "SUCCESS")
        if GPIO.input(CLOSE_PIN) == 0:
            if record_log.read_before_log()[2] != "LOCK": lock()
            record_log.write_log("BUTTON", "LOCK", "SUCCESS")

        # 自動開錠する時刻になったら開錠する
        dt_now = datetime.datetime.now()
        if dt_now.time() > open_time and dt_now.time() < diff_open_time:
            open()
            record_log.write_log("TIME", "OPEN", "SUCCESS")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+Cが押されたらGIPを初期化して終了
        open()
        print("cleanup...")
        GPIO.cleanup()
        exit(1)