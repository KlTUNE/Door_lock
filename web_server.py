from flask import Flask, request, jsonify
from modules import password_check, record_log
import main as lock_ctl

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
        if (password == "") {
            $('#message').html("パスワードを入力してください");
            return false;
        }
        let formdata = new FormData();
        formdata.append("pw", password);
        formdata.append("os", navigator.platform);
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
        let formdata = new FormData();
        formdata.append("os", navigator.platform);
        fetch("/open/", {
            method: "POST",
            body: formdata
        }).then(response => response.json()).then(data => {
            status = data["status"];
            if (status == "ok") {
                $('#message').html("施錠しました");
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

# /open/ にPOSTリクエストを送ると、開錠・施錠する
@app.route('/open/', methods=['POST'])
def open():
    try:
        password = request.form.get('pw', None)
        os = request.form.get('os', None)

        result = password_check.check(password)
        # パスワードが送られてこなかった場合、施錠する
        if password is None:
            if record_log.read_before_log()[2] != "LOCK": lock_ctl.lock()
            record_log.write_log(f"{request.remote_addr}[{os}]", "LOCK", "SUCCESS")
            return jsonify({'status': 'ok'})
        # パスワードが正しい場合、開錠する
        elif result:
            if record_log.read_before_log()[2] != "OPEN": lock_ctl.open()
            record_log.write_log(f"{request.remote_addr}[{os}]", "OPEN", "SUCCESS")
            return jsonify({'status': 'ok'})
        # パスワードが違う場合、施錠し、エラーを返す
        elif not result:
            record_log.write_log(f"{request.remote_addr}[{os}]", "ERROR", "PASSWORD ERROR")
            return jsonify({'status': 'error', 'message': 'パスワードが違います'})

    except Exception as e:
        record_log.write_log(f"{request.remote_addr}[{os}]", "ERROR", f"ERROR:{e}")
        return jsonify({'status': 'error', 'message': e})

# 開錠、施錠ができるWebページを表示する
@app.route('/')
def index():
    return HTML

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)