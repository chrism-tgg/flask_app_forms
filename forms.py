from flask_wtf import FlaskForm
# field types
from wtforms import (StringField, BooleanField, RadioField, EmailField)
# from wtforms.fields.html5 import EmailField
# validators
from wtforms.validators import InputRequired, Length


# define form fields
class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    organization = StringField('Organization', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    email = EmailField('Email', validators=[InputRequired(),
                                             Length(min=1, max=150)])
    # multiple choice
    level_q1 = RadioField('1: How often do you use data?',
                       choices=['1-never', '2-sometimes', '3-often', '4-always'],
                       validators=[InputRequired()])
    level_q2 = RadioField('2: How often do you use Excel?',
                       choices=['1-never', '2-sometimes', '3-often', '4-always'],
                       validators=[InputRequired()])
    level_q3 = RadioField('3: Long paragraph text. Lorem ipsum. The quick brown fox jumps over the lazy dog? The quick brown fox jumps over the lazy dog? The quick brown fox jumps over the lazy dog? The quick brown fox jumps over the lazy dog? The quick brown fox jumps over the lazy dog? The quick brown fox jumps over the lazy dog?',
                       choices=['1-never', '2-sometimes', '3-often', '4-always'],
                       validators=[InputRequired()])
    contact = BooleanField('Contact me about my results', default='checked')