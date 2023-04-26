import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask

load_dotenv(find_dotenv())

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

app = Flask(__name__, static_folder="flask_blog/static")
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.secret_key = SECRET_KEY