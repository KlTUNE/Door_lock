from flask import Flask, render_template, request, jsonify
from modules import lock_ctl, password_check

app = Flask(__name__)
# 開錠状態
LOCK_STATUS = "OPEN"

# /open/ にPOSTリクエストを送ると、パスワードをチェックして開錠する
@app.route('/open/', methods=['POST'])
def open():
    global LOCK_STATUS
    try:
        password = request.form.get('pw', None)
        if password_check.check(password) and LOCK_STATUS == "LOCK":
            lock_ctl.open()
            LOCK_STATUS = "OPEN"
        else: return jsonify({'status': 'error', 'message': 'パスワードが違います'})
        return jsonify({'status': 'ok'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': e})

# /lock/ にGETリクエストを送ると、施錠する
@app.route('/lock/')
def lock():
    global LOCK_STATUS
    try:
        if LOCK_STATUS == "OPEN":
            lock_ctl.lock()
            LOCK_STATUS = "LOCK"
        return jsonify({'status': 'ok'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': e})

# 開錠、施錠ができるWebページを表示する
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)