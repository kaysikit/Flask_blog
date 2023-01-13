from flask import render_template, redirect, url_for, session, flash

from flask_blog.forms.forms import RegistrationForm
from flask_blog.models.models import User


class RegistrationController:
    @staticmethod
    def call():
        if not session.get("name"):
            form = RegistrationForm()
            if form.validate_on_submit():
                res = User.new(
                    form.login.data,
                    form.password.data,
                )
                if res:
                    flash("Registration was successful", category="success")
                    return redirect(url_for("view.login"))
                else:
                    flash("Something went wrong, try again", category="error")
                    return redirect(url_for("view.register"))

        else:
            return redirect(url_for("view.main"))
        return render_template("register.html", form=form)
