from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    entrada = TextAreaField('entrada', validators=[DataRequired()])
    submit = SubmitField('submit')