from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class BaseForm(FlaskForm):
    login = StringField(
        "Login: ",
        validators=[
            DataRequired(),
            Length(
                min=6,
                max=30,
                message="The login must contain at least %(min)d characters",
            ),
            Regexp(
                '^\w+$',
                message="Valid characters [a-z], [A-Z], [0-9]",
            ),
        ],
    )
    password = PasswordField(
        "Password: ",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=100,
                message="The password must contain at least %(min)d characters",
            ),
        ],
    )


class RegistrationForm(BaseForm):
    submit = SubmitField("Registration")


class LoginForm(BaseForm):
    submit = SubmitField("Authorization")


class ReplacePasswordForm(FlaskForm):
    password_old = PasswordField(
        "Old password: ",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=100,
            ),
        ],
    )
    new_password1 = PasswordField(
        "New password: ",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=100,
                message="The password must contain at least %(min)d characters",
            ),
        ],
    )
    new_password2 = PasswordField(
        "Repeat password: ",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=100,
            ),
            EqualTo(
                "new_password1",
                message="Passwords must match",
            ),
        ],
    )
    submit = SubmitField("Change Password")
