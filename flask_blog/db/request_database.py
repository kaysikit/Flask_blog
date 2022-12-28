from flask_blog.models.models import *
import bcrypt

# Create tables in PostgreSQL
# import psycopg2
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


def add_user(login, psw) -> bool:
    user_exist = True
    try:
        check_user = User.select().where(User.login == login)
        if check_user:
            user_exist = False
    except DoesNotExist as de:
        user_exist = False

    if user_exist:
        row = User(login=login, password=psw)
        row.save()
        return True
    return False


def autenfication_user(login, psw) -> bool:
    try:
        check_password = User.get(User.login == login)
        salt = check_password.password.encode()
        if bcrypt.checkpw(psw, salt):
            return True
    finally:
        if db:
            db.close()

    return False


def get_all_users():
    return User.select(User.login, User.date_reg)


def get_profile(login):
    return User.select().where(User.login == login)


def replace_pass(login, new_psw1) -> bool:
    try:
        user = User.get(User.login == login)
        user.password = new_psw1
        user.save()
        return True
    finally:
        if db:
            db.close()

    return False


def replace_avatar(login, filename) -> bool:
    try:
        user = User.get(User.login == login)
        user.avatar = 'img/users/' + filename
        user.save()
        return True
    finally:
        if db:
            db.close()

    return False
