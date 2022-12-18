import os

import bcrypt
from flask import render_template, redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename

from config import ALLOWED_EXTENSION
from flask_blog.db.request_database import add_user, autenfication_user, view_all_users, view_profile, replace_pass, \
    replace_avatar
from flask_blog.forms.forms import RegistrationForm, LoginForm, ReplacePasswordForm


def check_auth(func):
    def wrapper(*args, **kwargs):
        login = session.get("name")
        if login:
            return func(*args, **kwargs)
        return redirect(url_for('view.login'))

    return wrapper


class RegistrationController:
    def call():
        if not session.get("name"):
            form = RegistrationForm()
            if form.validate_on_submit():
                res = add_user(form.login.data, bcrypt.hashpw(form.psw.data.encode(), bcrypt.gensalt(14)))
                if res:
                    flash('Регистрация прошла успешно', category='success')
                    return redirect(url_for('view.login'))
                else:
                    flash('Что-то пошло не так, попробуйте ещё раз', category='error')
                    return redirect(url_for('view.register'))
        else:
            return redirect(url_for('view.main'))
        return render_template("register.html", form=form)


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
                    flash('Неправильно введён логин или пароль', category='error')
                    return redirect(url_for('view.login'))
        else:
            return redirect(url_for('view.main'))
        return render_template("login.html", form=form)


class UsersController:
    @check_auth
    def view():
        users = view_all_users()
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
        user = view_profile(session.get("name"))
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

    def replace_psw(self, form):
        if not autenfication_user(self, form.psw_old.data.encode()):
            flash('Неверно введён старый пароль', category='error')
            return redirect(url_for('view.profile'))
        else:
            res = replace_pass(self, bcrypt.hashpw(form.new_psw1.data.encode(), bcrypt.gensalt(14)))
            if res:
                flash('Пароль изменён', category='success')
                return redirect(url_for('view.profile'))
            else:
                flash('Что-то пошло не так, попробуйте ещё раз', category='error')
                return redirect(url_for('view.profile'))


class FilesController:
    def allowed_file(self, file):
        filename = file.filename
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

    @check_auth
    def upload_avatar():
        if request.method == 'POST':
            login = session.get("name")
            file = request.files['file']
            if file and FilesController.allowed_file(file):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.getenv('UPLOAD_FOLDER'), filename))
                res = replace_avatar(login, filename)
                if res:
                    flash('Аватарка изменена', category='success')
                return redirect(url_for('view.profile'))
