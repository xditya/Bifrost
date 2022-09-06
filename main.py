from flask import Flask, render_template, request

app = Flask(__name__)

ips = []


@app.route("/")
def home_page():
    ip = request.environ["REMOTE_ADDR"]
    print("IP:", ip)
    return portal_clicked() if ip in ips else render_template("index.html")


@app.route("/portal2")
def portal_clicked():
    ip = request.remote_addr
    if ip not in ips:
        ips.append(ip)
    return render_template("landing.html", booking_id=f"#{len(ips) + 1}")


app.run(debug=True)
# do not use app.run in production
