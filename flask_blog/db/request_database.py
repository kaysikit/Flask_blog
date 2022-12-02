from flask_blog.db.connect_db import *
from datetime import datetime, timezone
from flask_blog.models.models import *
import psycopg2
import bcrypt

# try:
#     with db:
#         db.create_tables([User])
#
# except Exception as ex:
#     print("[INFO] Error while working with PostgreSQL", ex)
#
# finally:
#     if db:
#         db.close()
#         print("[INFO] PostgreSQL connection close")
db.autocommit = True


def add_user(login, psw):
    user_exist = True
    dt = datetime.datetime.now(timezone.utc)
    try:
        check_user = User.select().where(User.login == login)
        if check_user:
            user_exist = False
    except DoesNotExist as de:
        user_exist = False

    if user_exist:
        row = User(login=login, password=psw, date_reg=dt)
        row.save()
        return True
    return False


def autenfication_user(login, psw):
    try:
        check_password = User.get(User.login == login)
        salt = check_password.password.encode()
        if bcrypt.checkpw(psw, salt):
            return True
    except Exception as ex:
        print(ex)

    return False

def view_users():
    return User.select()
