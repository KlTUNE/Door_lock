from flask import Flask, render_template, request, jsonify
from modules import lock_ctl, password_check, record_log

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

# /open/ にPOSTリクエストを送ると、パスワードをチェックして開錠する
@app.route('/open/', methods=['POST'])
def open():
    try:
        password = request.form.get('pw', None)
        if password_check.check(password):
            if record_log.read_before_log()[2] == "LOCK": lock_ctl.open()
            record_log.write_log(request.remote_addr, "OPEN", "SUCCESS")
        else:
            record_log.write_log(request.remote_addr, "ERROR", "PASSWORD ERROR")
            return jsonify({'status': 'error', 'message': 'パスワードが違います'})
        return jsonify({'status': 'ok'})

    except Exception as e:
        record_log.write_log(request.remote_addr, "ERROR", f"ERROR:{e}")
        return jsonify({'status': 'error', 'message': e})

# /lock/ にGETリクエストを送ると、施錠する
@app.route('/lock/')
def lock():
    try:
        if record_log.read_before_log()[2] == "OPEN": lock_ctl.lock()
        record_log.write_log(request.remote_addr, "LOCK", "SUCCESS")
        return jsonify({'status': 'ok'})

    except Exception as e:
        record_log.write_log(request.remote_addr, "ERROR", f"ERROR:{e}")
        return jsonify({'status': 'error', 'message': e})

# 開錠、施錠ができるWebページを表示する
@app.route('/')
def index():
    # return render_template("index.html")
    return HTML

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)