from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/history")
def test():
    return render_template("history.html")


@app.route("/charectericts")
def char():
    return render_template("charectericts.html")


@app.route("/fotos")
def foto():
    return render_template("fotos.html")


app.run(debug=True)
