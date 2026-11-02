from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MorseCode(FlaskForm):
    text_to_convert = StringField("Entry:",validators=[DataRequired()])
    submit = SubmitField("Convert")