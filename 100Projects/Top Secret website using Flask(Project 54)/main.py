from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
import os
from dotenv import load_dotenv
from forms import LoginForm

load_dotenv()

secret_email = os.getenv("SECRET_EMAIL")

secret_password = os.getenv("SECRET_PASSWORD")


app = Flask(__name__)
bootstrap = Bootstrap4(app=app)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == secret_email and form.password.data == secret_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
