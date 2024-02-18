from flask import Flask, render_template, request, jsonify
from modules import lock_ctl, password_check

app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html lang="jp">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOOR LOCK WEB</title>
    <style>
    </style>
</head>
<body>
    <h1>DOOR LOCK WEB</h1>
    <p id="message"> </p>
    <input type="password" id="password" placeholder="パスワードを入力してください">
    <button id="open" onclick="_open()">開ける</button>
    <button id="close" onclick="lock()">閉める</button>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
    function _open() {
        $('#message').html("");
        let password = $('#password').val();
        console.log(password);
        if (password == "") {
            $('#message').html("パスワードを入力してください");
            return false;
        }
        let formdata = new FormData();
        formdata.append("pw", password);
        fetch("/open/", {
            method: "POST",
            body: formdata
        }).then(response => response.json()).then(data => {
            status = data["status"];
            if (status == "ok") {
                $('#message').html("開錠しました");
            }
            else if (status == "error"){
                $('#message').html(data["message"]);
            }
        })
        .catch(error => {
            console.error('エラー:', error);
        });
        $('#password').val("");
    }

    function lock() {
        $('#message').html("");
        fetch("/lock/", {
            method: "GET"
        }).then(response => response.json()).then(data => {
            status = data["status"];
            if (status == "ok") {
                $('#message').html("ロックしました");
            }
            else if (status == "error"){
                $('#message').html(data["message"]);
            }
        })
        .catch(error => {
            console.error('エラー:', error);
        });
    }
</script>
</html>
"""

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
    # return render_template("index.html")
    return HTML

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)