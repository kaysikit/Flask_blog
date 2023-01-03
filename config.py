import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
