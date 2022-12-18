from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo


class BaseForm(FlaskForm):
    login = StringField("Логин: ", validators=[DataRequired(), Length(min=6, max=30,
                                                                      message='Логин должен содержать не менее %(min)d символов')])
    psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=8, max=100,
                                                                       message='Пароль должен содержать не менее %(min)d символов')])

    def validate_login(self, login):
        excluded_chars = " *?!'^+%&;/()=}][{$#"
        for char in self.login.data:
            if char in excluded_chars:
                raise ValidationError(
                    f"Символ {char} недопустим в логине"
                )


class RegistrationForm(BaseForm):
    submit = SubmitField("Регистрация")


class LoginForm(BaseForm):
    submit = SubmitField("Авторизация")


class ReplacePasswordForm(FlaskForm):
    psw_old = PasswordField("Старый пароль: ", validators=[DataRequired(), Length(min=8, max=100)])
    new_psw1 = PasswordField("Новый пароль: ", validators=[DataRequired(), Length(min=8, max=100,
                                                                                  message='Пароль должен содержать не менее %(min)d символов')])
    new_psw2 = PasswordField("Повторить пароль: ",
                             validators=[DataRequired(), Length(min=8, max=100),
                                         EqualTo('new_psw1', message='Пароли должны совпадать')])
    submit = SubmitField("Изменить пароль")
