from flask import Flask, render_template, request, jsonify, make_response, redirect
from modules import lock_ctl, password_check

app = Flask(__name__)

@app.route('/open/', methods=['POST'])
def open():
    try:
        print("アクセス")
        password = request.form.get('pw', None)
        print(password)
        if password_check.check(password): lock_ctl.open()
        else: return jsonify({'status': 'error', 'message': 'パスワードが違います'})
        return jsonify({'status': 'ok'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': e})

@app.route('/lock/')
def lock():
    try:
        lock_ctl.lock()
        return jsonify({'status': 'ok'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': e})

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=80)