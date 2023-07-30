from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from forms import CafeForm
import csv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(file="cafe-data.csv", mode="a") as csv_file:
            csv_file.write( f"\n{form.cafe.data},"
                            f"{form.Location_URL.data},"
                            f"{form.open_time.data},"
                            f"{form.close_time.data},"
                            f"{form.coffee_rating.data},"
                            f"{form.wifi_rating.data},"
                            f"{form.power_outlet_rating.data}"
                           )
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
