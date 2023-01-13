from flask import render_template, redirect, url_for, session, flash
from playhouse.flask_utils import object_list

from flask_blog.models.models import User
from flask_blog.forms.forms import ReplacePasswordForm


def check_auth(func):
    def wrapper(*args, **kwargs):
        login = session.get("name")
        if login:
            return func(*args, **kwargs)
        return redirect(url_for("view.login"))

    return wrapper


class UsersController:
    @staticmethod
    @check_auth
    def view():
        users = User.get_all()
        return object_list(
            'view.html',
            query=users,
            context_variable='user_list',
            paginate_by=10,
            page_var='page',
        )

    @staticmethod
    @check_auth
    def logout():
        session["name"] = None
        return redirect(url_for("view.main"))

    @staticmethod
    @check_auth
    def profile():
        user = User.get_profile(session.get("name"))
        form = ReplacePasswordForm()
        login = session.get("name")
        if form.validate_on_submit():
            UsersController.update_password(login, form)
        return render_template("profile.html", user=user, form=form)

    @staticmethod
    @check_auth
    def update_password(login, form):
        if not User.autenfication(login, form.password_old.data.encode()):
            flash("The old password was entered incorrectly", category="error")
            return redirect(url_for("view.profile"))
        else:
            res = User.update_password(
                login,
                form.new_password1.data,
            )
            if res:
                flash("Password changed", category="success")
                return redirect(url_for("view.profile"))
            else:
                flash("Something went wrong, try again", category="error")
                return redirect(url_for("view.profile"))
