from flask import Blueprint

from flask_blog.controllers.files import FilesController
from flask_blog.controllers.users import UsersController

user = Blueprint("user", __name__, template_folder="../templates")


@user.route("/view/", methods=["GET"])
def view_users():
    return UsersController.view()


@user.route("/profile", methods=["POST", "GET"])
def profile():
    return UsersController.profile()


@user.route("/upload_avatar", methods=["POST"])
def upload_avatar():
    return FilesController.upload_avatar()
