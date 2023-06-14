from flask import Blueprint

from flask_blog.controllers.authorization import AuthorizationController
from flask_blog.controllers.registration import RegistrationController
from flask_blog.controllers.users import UsersController

autenfication = Blueprint('autenfication', __name__, template_folder="../templates")


@autenfication.route("/register", methods=["POST", "GET"])
def register():
    return RegistrationController.call()


@autenfication.route("/login", methods=["POST", "GET"])
def login():
    return AuthorizationController.call()


@autenfication.route("/logout")
def logout():
    return UsersController.logout()
