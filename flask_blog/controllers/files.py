import mimetypes
import os
import uuid

from flask import redirect, url_for, session, request, flash

from config import UPLOAD_FOLDER
from flask_blog.controllers.users import check_auth
from flask_blog.models.models import User


class FilesController:
    def __init__(self, file):
        self.filename = file.filename

    @staticmethod
    def allowed_file(file):
        allowed_mimetypes = ["image/jpeg", "image/png"]
        if mimetypes.guess_type(file.filename)[0] in allowed_mimetypes:
            return True
        return False


    @staticmethod
    @check_auth
    def upload_avatar():
        if request.method == "POST":
            login = session.get("name")
            file = request.files["file"]
            if file and FilesController.allowed_file(file):
                filename = (
                    str(uuid.uuid4()) + "." + file.filename.rsplit(".", 1)[1].lower()
                )
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                res = User.update_avatar(login, filename)
                if res:
                    flash("Avatar changed", category="success")
            else:
                flash("Use png or jpeg format", category="error")
            return redirect(url_for("view.profile"))
