from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy()
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    query = db.session.execute(db.select(Books).order_by(Books.id))
    all_books = query.scalars().all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Books(
                title=request.form["Book Name"],
                author=request.form["Author"],
                rating=request.form["Rating"]
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["POST", "GET"])
def edit_rating(book_id):
    book = db.get_or_404(Books, book_id)
    print(book.id)
    if request.method == "POST":
        new_rating = request.form["Change Rating"]
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", selected_book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Books, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

