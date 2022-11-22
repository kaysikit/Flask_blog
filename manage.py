# -*- coding: utf8 -*-
from flask import Flask, render_template, request
from flask_blog.db.connect_db import *
from config import *
from flask_blog.models.models import *
import psycopg2
from flask_blog.forms.forms import RegistrationForm, LoginForm

# try:
#     with db:
#         db.create_tables([User])
#
# except Exception as ex:
#     print("[INFO] Error while working with PostgreSQL", ex)
#
# finally:
#     if db:
#         db.close()
#         print("[INFO] PostgreSQL connection close")

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return render_template('base.html')


@app.route("/register")
def register():
    return "<h1>Hello</h1>"


@app.route("/login")
def login():
    form = LoginForm
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
