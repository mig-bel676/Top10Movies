from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from db import db, Movies
from forms import movieForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movies.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    addingForm = movieForm()
    return render_template("add.html", form=addingForm)




if __name__ == '__main__':
    app.run(debug=True, port=5009)
