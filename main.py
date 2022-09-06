import string
from random import choice

from flask import Flask, render_template, request

app = Flask(__name__)

ips = {}


@app.route("/")
def home_page():
    ip = request.environ["REMOTE_ADDR"]
    print("IP:", ip)
    return portal_clicked() if ip in ips else render_template("index.html")


@app.route("/portal2")
def portal_clicked():
    ip = request.remote_addr
    random_booking_id = "".join(
        [choice(string.ascii_letters + string.digits) for _ in range(10)]
    )
    if ip not in list(ips.keys()):
        ips[ip] = random_booking_id
    return render_template("landing.html", booking_id=f"{random_booking_id}")


app.run(debug=True)
# do not use app.run in production
