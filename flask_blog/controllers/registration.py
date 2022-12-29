from flask import render_template, redirect, url_for, session, flash

from flask_blog.db.request_database import add_user
from flask_blog.forms.forms import RegistrationForm
import bcrypt


class RegistrationController:
    def call():
        if not session.get("name"):
            form = RegistrationForm()
            if form.validate_on_submit():
                res = add_user(form.login.data, bcrypt.hashpw(form.psw.data.encode(), bcrypt.gensalt(14)))
                if res:
                    flash('Registration was successful', category='success')
                    return redirect(url_for('view.login'))
                else:
                    flash('Something went wrong, try again', category='error')
                    return redirect(url_for('view.register'))
        else:
            return redirect(url_for('view.main'))
        return render_template("register.html", form=form)
