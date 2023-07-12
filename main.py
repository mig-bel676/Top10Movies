from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sqlalchemy.exc import SQLAlchemyError
from db import db, Movies
from forms import movieForm, quickForm
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
    # Read rows of data from Movies database and passover list of movie objects to html page
    movie_List = Movies.query.all()
    return render_template("index.html", movies=movie_List)


@app.route("/add", methods=["GET", "POST"])
def add():
    addingForm = movieForm()
    if addingForm.validate_on_submit():
        print("If statment worked")
        # Create new data entry for Movies database
        with app.app_context():
            new_Movie = Movies(
                title=addingForm.movie_Title.data,
                year=addingForm.year.data,
                rating=addingForm.movie_Rating.data,
                comments=addingForm.movie_Comments.data,
                summary=addingForm.movie_Summary.data
            )
            try:
                db.session.add(new_Movie)
                db.session.commit()
                print("Transaction Successful ")
            except SQLAlchemyError as error:
                db.session.rollback()
                print(f"Error occured during transaction: {error}")
                return redirect(url_for('add'))
        return redirect(url_for('home'))
    return render_template("add.html", form=addingForm)


@app.route('/update', methods=["GET", "POST"])
def update():
    editForm = quickForm()
    movie_ID = request.args.get('id')
    movie_Selected = db.get_or_404(Movies, movie_ID)
    if editForm.validate_on_submit():
        movie_Selected.rating = editForm.new_Rating.data
        movie_Selected.comments = editForm.new_Comment.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=editForm, movie=movie_Selected)


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    movie_Selected = db.get_or_404(Movies, id)
    db.session.delete(movie_Selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5009)
