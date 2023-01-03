import mimetypes
import os
import uuid

from flask import redirect, url_for, session, request, flash

from config import UPLOAD_FOLDER
from flask_blog.controllers.users import check_auth
from flask_blog.db.request_database import replace_avatar


class FilesController:
    def __init__(self, file):
        self.filename = file.filename
    def allowed_file(self):
        allowed_mimetypes = ['image/jpeg', 'image/png' ]
        if mimetypes.guess_type(self.filename)[0] in allowed_mimetypes:
            return True
        return False


    @check_auth
    def upload_avatar():
        if request.method == 'POST':
            login = session.get("name")
            file = request.files['file']
            if file and FilesController.allowed_file(file):
                filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                res = replace_avatar(login, filename)
                if res:
                    flash('Avatar changed', category='success')
            else:
                flash('Use png or jpeg format', category='error')
            return redirect(url_for('view.profile'))