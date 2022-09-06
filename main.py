from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/portal2")
def portal_clicked():
    return "Thanks for clicking"


app.run(debug=True)
# do not use app.run in production
