from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template("start.html")

app.run()