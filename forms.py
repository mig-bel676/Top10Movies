from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired


class movieForm(FlaskForm):
    movie_Title = StringField(label='Name', validators=[DataRequired()])
    year = IntegerField(label='Year', validators=[DataRequired()])
    movie_Rating = FloatField(label='Rating', validators=[DataRequired()])
    movie_Comments = StringField(label='Your Review', validators=[DataRequired()])
    movie_Summary = TextAreaField(label='Summary', validators=[DataRequired()])
    submit = SubmitField("Submit")


class quickForm(FlaskForm):
    new_Rating = FloatField(label='Your Rating out of 10 e.g. 6.5', validators=[DataRequired()])
    new_Comment = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField("Submit")