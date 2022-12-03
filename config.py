import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
db_name = os.getenv('DB_NAME')
