from flask_wtf import FlaskForm
# field types
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
# validators
from wtforms.validators import InputRequired, Length


# define form fields
class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    # multiple choice
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')