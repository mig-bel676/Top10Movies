from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comments = db.Column(db.String(250), nullable=False)
    summary = db.Column(db.String(300))

    def __init__(self, title, year, rating, comments, summary):
        self.title = title
        self.year = year
        self.rating = rating
        self.comments = comments
        self.summary = summary

    # Optional: this will allow each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie: {self.title}>'