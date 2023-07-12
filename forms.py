from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired


class movieForm(FlaskForm):
    movie_Title = StringField(label='Name', validators=[DataRequired()])
    year = IntegerField(label='Year', validators=[DataRequired()])
    movie_Rating = FloatField(label='Rating', validators=[DataRequired()])
    movie_Comments = StringField(label='Critic Comment', validators=[DataRequired()])
    movie_Summary = TextAreaField(label='Summary', validators=[DataRequired()])
    submit = SubmitField("Submit")