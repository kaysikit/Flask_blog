from flask_blog.models.models import *
import bcrypt
import datetime

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


def get_all_users() -> object:
    return User.select(User.login, User.create_at)


def get_profile(login: object) -> object:
    return User.select().where(User.login == login)


def replace_pass(login, new_psw1) -> bool:
    try:
        user = User.get(User.login == login)
        user.password = new_psw1
        user.update_at = datetime.datetime.now()
        user.save()
        return True
    finally:
        if db:
            db.close()

    return False


def replace_avatar(login, filename) -> bool:
    try:
        user = User.get(User.login == login)
        user.avatar = "img/users/" + filename
        user.update_at = datetime.datetime.now()
        user.save()
        return True
    finally:
        if db:
            db.close()

    return False
