from flask import Flask, render_template, requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if requests.method == "POST":
    return render_template("index.html")


app.run(debug=True, port=5001)