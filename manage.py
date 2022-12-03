# -*- coding: utf8 -*-
import os
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session
from config import *
from flask_blog.models.models import *
from flask_blog.forms.forms import RegistrationForm, LoginForm
from flask_blog.db.request_database import add_user, autenfication_user, view_all_users
from flask_session import Session

app = Flask(__name__, template_folder='flask_blog/templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/register", methods=["POST", "GET"])
def register():
    if not session.get("name"):
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User()
            user.login = form.login.data
            user.password = bcrypt.hashpw(form.psw.data.encode(), bcrypt.gensalt(14))
            res = add_user(user.login, user.password)
            if res:
                return redirect(url_for('login'))
            else:
                return redirect(url_for('register'))
    else:
        return redirect(url_for('main'))
    return render_template("register.html", form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if not session.get("name"):
        form = LoginForm()
        if form.validate_on_submit():
            user = User()
            user.login = form.login.data
            user.password = form.psw.data.encode()
            res = autenfication_user(user.login, user.password)
            if res:
                session["name"] = user.login
                return redirect(url_for('main'))
            else:
                return redirect(url_for('login'))
    else:
        return redirect(url_for('main'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect(url_for('main'))


@app.route('/view')
def view_users():
    if session.get("name"):
        users = view_all_users()
        users_list = []
        for user in users:
            users_list.append({
                'login': user.login,
                'date_reg': user.date_reg
            })
    else:
        return redirect(url_for('login'))
    return render_template('view.html', users_list=users_list)


if __name__ == "__main__":
    app.run(debug=True)
