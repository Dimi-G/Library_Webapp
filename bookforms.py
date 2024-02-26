# Inheriting from class FlaskForm, we create child class with the form fields of our choice for the book additions or corrections
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class AddForm(FlaskForm):
    book_title = StringField('Book Title', validators=[DataRequired()])
    book_author=StringField('Author', validators=[DataRequired()])
    rating=FloatField('Rating: 0-10', validators=[InputRequired(),NumberRange(min=0, max=10, message='Please enter a number between 0-10')])
    submit = SubmitField('Add Book')  

class EditForm(FlaskForm):
    new_rating=FloatField('New Rating', validators=[InputRequired(),NumberRange(min=0, max=10, message='Please enter a number between 0-10')])
    submit = SubmitField('Change Rating') 