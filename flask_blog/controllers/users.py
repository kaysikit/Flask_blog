import bcrypt
from flask import render_template, redirect, url_for, session, flash

from flask_blog.db.request_database import autenfication_user, get_all_users, get_profile, replace_pass
from flask_blog.forms.forms import ReplacePasswordForm


def check_auth(func):
    def wrapper(*args, **kwargs):
        login = session.get("name")
        if login:
            return func(*args, **kwargs)
        return redirect(url_for('view.login'))

    return wrapper


class UsersController:
    @check_auth
    def view():
        users = get_all_users()
        users_list = []
        for user in users:
            users_list.append({
                'login': user.login,
                'date_reg': user.date_reg
            })
        return render_template('view.html', users_list=users_list)

    @check_auth
    def logout():
        session["name"] = None
        return redirect(url_for('view.main'))

    @check_auth
    def profile():
        user = get_profile(session.get("name"))
        user_list = []
        for item in user:
            user_list.append({
                'login': item.login,
                'date_reg': item.date_reg,
                'avatar': item.avatar
            })
        form = ReplacePasswordForm()
        login = session.get("name")
        if form.validate_on_submit():
            UsersController.replace_psw(login, form)
        return render_template('profile.html', user_list=user_list, form=form)

    @check_auth
    def replace_psw(self, form):
        if not autenfication_user(self, form.psw_old.data.encode()):
            flash('The old password was entered incorrectly', category='error')
            return redirect(url_for('view.profile'))
        else:
            res = replace_pass(self, bcrypt.hashpw(form.new_psw1.data.encode(), bcrypt.gensalt(14)))
            if res:
                flash('Password changed', category='success')
                return redirect(url_for('view.profile'))
            else:
                flash('Something went wrong, try again', category='error')
                return redirect(url_for('view.profile'))
