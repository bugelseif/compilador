from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    entrada = TextAreaField('Entrada', validators=[DataRequired()])
    submit = SubmitField('submit')