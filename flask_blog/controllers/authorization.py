from flask import render_template, redirect, url_for, session, flash

from flask_blog.models.models import User
from flask_blog.forms.forms import LoginForm


class AuthorizationController:
    @staticmethod
    def call():
        if not session.get("name"):
            form = LoginForm()
            if form.validate_on_submit():
                res = User.autenfication(
                    form.login.data,
                    form.password.data,
                )
                if res:
                    session["name"] = form.login.data
                    return redirect(url_for("misc.main"))
                else:
                    flash("Login or password entered incorrectly", category="error")
                    return redirect(url_for("view.login"))
        else:
            return redirect(url_for("view.main"))
        return render_template("login.html", form=form)
