from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv
import requests

load_dotenv()

my_mail = os.getenv("MY_MAIL")
app_password = os.getenv("APP_PASSWORD")

app = Flask(__name__)

n_point = os.getenv("N_POINT")
data = requests.get(url=n_point).json()


def send_mail(name, email, phone, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=app_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=my_mail,
            msg=f"Subject:Message from {name}\n\nemail: {email}\nphone: {phone}\nmessage: {msg}\n"
        )


@app.route("/")
def home():
    return render_template("index.html", posts=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["message"]
        send_mail(name, email, phone, msg)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:id>")
def expand_post(id):
    clicked_post = data[id - 1]
    return render_template("post.html", post=clicked_post)


if __name__ == "__main__":
    app.run(debug=True)
