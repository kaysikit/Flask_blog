from flask import redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSION
import os

from flask_blog.db.request_database import replace_avatar


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
                    flash('Avatar changed', category='success')
                return redirect(url_for('view.profile'))
