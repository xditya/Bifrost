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


@app.route("/portal")
def portal_clicked():
    portal_number = request.args.get("id")
    if not portal_number:
        return "404."
    ip = request.remote_addr
    random_booking_id = "".join(
        [choice(string.ascii_letters + string.digits) for _ in range(10)]
    )
    if ip not in list(ips.keys()):
        ips[ip] = random_booking_id
    return render_template(
        "landing.html", booking_id=random_booking_id, portal_number=portal_number
    )


app.run(debug=True)
# do not use app.run in production
