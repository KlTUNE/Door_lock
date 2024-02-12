# ドアロック
## 現状のバグ・問題点

## 概要
指紋認証、HTTPリクエストにより開錠することができる。  
内側からは、ボタン操作により施錠・開錠を行うことができる。  

## 実行方法
<pre>
pip install pyfingerprint
pip install RPi.GPIO
pip install flask
        or
pip install -r requirements.txt

python3 main.py
</pre>

## プログラム
### pinアサイン
![RaspberryPIのピンアサインの画像](https://camo.qiitausercontent.com/d47eb1c4132a524c410f6eab25e03c36a1fbe271/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f313131353239312f32666365326566332d396434332d313361392d396465342d6433336164323936626139302e706e67)

### プログラム一覧
- main.py
    - 指紋認証モジュール、内側のボタンからの入力の監視、制御を行う。
    - また、web_server.pyをマルチスレッドを利用し、別スレッドで立ち上げる。
- web_server.py
    - FLASKを利用してwebサーバーを立ち上げ、HTTPリクエストを処理する。
- fp_ctl.py
    - 指紋認証モジュールを制御するためのプログラム。
    - main.pyから呼び出される。
- lock_ctl.py
    - サーボモーター、LEDなどを制御し、実査に施錠・開錠を行う。
    - main.py、web_server.pyから呼び出される.
- password_check.py
    - HTTPリクエストにより送られてきた解錠のためのパスワードの認証を行う。
    - web_server.pyから呼び出される。