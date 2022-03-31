from re import T
from flask import Flask, render_template, request
from tts import tts_output

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/tts", methods=["GET", "POST"])
def execute_tts():
    if request.method == "POST":
        text = request.form.get("text")
        tts_output(text)
        return "<h1>Form submitted ! Check console !</h1>"


app.run(debug=True)
