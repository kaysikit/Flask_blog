from flask import render_template, Blueprint

from flask_blog.controllers.authorization import AuthorizationController
from flask_blog.controllers.files import FilesController
from flask_blog.controllers.registration import RegistrationController
from flask_blog.controllers.users import UsersController

view = Blueprint("view", __name__, template_folder="../templates")


@view.route("/")
def main():
    return render_template("main.html")


@view.route("/register", methods=["POST", "GET"])
def register():
    return RegistrationController.call()


@view.route("/login", methods=["POST", "GET"])
def login():
    return AuthorizationController.call()


@view.route("/logout")
def logout():
    return UsersController.logout()


@view.route("/view")
def view_users():
    return UsersController.view()


@view.route("/profile", methods=["POST", "GET"])
def profile():
    return UsersController.profile()


@view.route("/upload_avatar", methods=["POST"])
def upload_avatar():
    return FilesController.upload_avatar()
