import os
from flask import Flask
from flask_session import Session
from flask_blog.views.view import view

app = Flask(__name__, static_folder='flask_blog/static')
app.register_blueprint(view, url_prefix="")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
Session(app)

if __name__ == "__main__":
    app.run(debug=True)
