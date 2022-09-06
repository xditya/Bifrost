import os
import string
from random import choice

from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder="static")


ips = {}


@app.route("/")
def home_page():
    ip = request.environ["REMOTE_ADDR"]
    # print("IP:", ip)
    return portal_clicked() if ip in ips else render_template("index.html")


@app.route("/confirm")
def confirm():
    portal_number = request.args.get("id")
    return (
        render_template("confirm.html", portal_id=portal_number)
        if portal_number
        else render_template("404.html")
    )


@app.route("/portal")
def portal_clicked():
    portal_number = request.args.get("id")
    if not portal_number:
        return render_template("404.html")
    ip = request.remote_addr
    random_booking_id = "".join(
        [choice(string.ascii_letters + string.digits) for _ in range(10)]
    )
    if ip not in list(ips.keys()):
        ips[ip] = random_booking_id
    return render_template(
        "landing.html", booking_id=random_booking_id, portal_number=portal_number
    )


@app.route("/cancel")
def canceller():
    portal_number = request.args.get("id")
    if not portal_number:
        return render_template("404.html")
    ip = request.remote_addr
    if ip in list(ips.keys()):
        ips.pop(ip)
    return redirect("/")


# app.run(debug=True, port=5000)
# app.run(debug=True, port=8080)
