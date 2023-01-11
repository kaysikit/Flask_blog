from flask import render_template, redirect, url_for, session, flash
import bcrypt

from flask_blog.forms.forms import RegistrationForm
from flask_blog.models.models import User


class RegistrationController:
    def call():
        if not session.get("name"):
            form = RegistrationForm()
            if form.validate_on_submit():
                res = User.new(
                    form.login.data,
                    bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt(14)),
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
