from flask import render_template, redirect, url_for, session, flash

from flask_blog.db.request_database import autenfication_user
from flask_blog.forms.forms import LoginForm


class AuthorizationController:
    def call():
        if not session.get("name"):
            form = LoginForm()
            if form.validate_on_submit():
                res = autenfication_user(form.login.data, form.psw.data.encode())
                if res:
                    session["name"] = form.login.data
                    return redirect(url_for('view.main'))
                else:
                    flash('Login or password entered incorrectly', category='error')
                    return redirect(url_for('view.login'))
        else:
            return redirect(url_for('view.main'))
        return render_template("login.html", form=form)
