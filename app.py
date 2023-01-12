from flask import Flask

from config import SECRET_KEY, UPLOAD_FOLDER
from flask_blog.views.view import view
from flask_session import Session

app = Flask(__name__, static_folder="flask_blog/static")
app.register_blueprint(view, url_prefix="")
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.secret_key = SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
Session(app)

if __name__ == "__main__":
    app.run(debug=True)
