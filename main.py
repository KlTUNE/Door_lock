from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def registration_show():
    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')