from wtforms import Form, StringField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class BaseForm(Form):
    login = StringField("Login: ", validators=[DataRequired(), Length(min=6, max=30)])
    psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=8, max=100)])


class RegistrationForm(BaseForm):
    submit = SubmitField("Регистрация")


class LoginForm(BaseForm):
    submit = SubmitField("Авторизация")
