from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Connecting to log in manager
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


def check_password(user, entered_password):
    if check_password_hash(pwhash=user.password, password=entered_password):
        login_user(user=user)
        return True
    else:
        return False


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        entered_email = request.form.get("email")
        user = db.session.execute(db.select(User).where(User.email == entered_email)).scalar()
        if user:
            flash(message="You've Already Signed up with that email, Log in Instead", category="error")
            return redirect(url_for("login"))
        hashed_and_salted_password = generate_password_hash(
            password=request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=8)
        with app.app_context():
            new_user = User(
                email=request.form.get("email"),
                password=hashed_and_salted_password,
                name=request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_email = request.form.get("email")
        entered_password = request.form.get("password")
        try:
            user = db.session.execute(db.select(User).where(User.email == entered_email)).scalar()
            if check_password(user, entered_password):
                return redirect(url_for("secrets"))
            else:
                flash(message="Incorrect Password", category="error")
                return render_template("login.html")
        except AttributeError:
            flash(message="Email is not registered yet", category="error")
            return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory='static', path="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
