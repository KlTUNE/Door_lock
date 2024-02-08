from flask import Flask, render_template, request, jsonify, make_response, redirect

app = Flask(__name__)

@app.route('/')
def mainn():
    return redirect("https://kitune-udon.com")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')