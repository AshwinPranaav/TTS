from re import T
from flask import Flask, render_template, request, Response
from tts import tts_output

app = Flask(__name__)


@app.route("/")
def hello_world():
    return Response(render_template("index.html"), headers = {"Cache-Control": "no-store"})


@app.route("/tts", methods=["GET", "POST"])
def execute_tts():
    if request.method == "POST":
        doc = request.files.get("document")
        if doc:
            text = open(doc.filename).read()
            
        else:
            text = request.form.get("text")
        tts_output(text)
    return Response(render_template("index.html", audio_file= "/static/text.wav"), headers = {"Cache-Control": "no-store"})


app.run(debug=True)
