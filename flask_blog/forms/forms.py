from flask_wtf import FlaskForm
from wtforms import Form, StringField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    login = StringField("Login: ", validators=[DataRequired(), Length(min=6, max=30)])
    psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=8, max=100)])
    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    login = StringField("Login: ", validators=[DataRequired(), Length(min=6, max=30)])
    psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=8, max=100)])
    submit = SubmitField("Авторизация")
