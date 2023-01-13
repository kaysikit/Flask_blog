from typing import Optional

import bcrypt
from peewee import *
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD
import datetime

# Connect with database PostgreSQL
db = PostgresqlDatabase(
    database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)
db.autocommit = True


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    login = TextField()
    password = CharField()
    create_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = TextField(null=True)
    avatar = CharField(default="img/default/avatar.png")

    # Create new user
    @classmethod
    def new(cls, login: str, password: str) -> Optional['User']:
        user_exist = cls.select().where(cls.login == login).exists()
        if user_exist:
            return None

        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(14))
        user = User(login=login, password=password)
        user.save()
        return user

    # User authorization
    @classmethod
    def autenfication(cls, login: str, password: str) -> bool | None:
        user_exist = cls.select().where(cls.login == login).exists()
        if not user_exist:
            return None

        password = password.encode()
        check_password = cls.get(cls.login == login)
        salt = check_password.password.encode()
        if bcrypt.checkpw(password, salt):
            return True

    # Getting a list of all users
    @classmethod
    def get_all(cls) -> object:
        return cls.select(cls.login, cls.create_at)

    # Getting an authorized user
    @classmethod
    def get_profile(cls, login) -> object:
        return cls.select(
            cls.login,
            cls.create_at,
            cls.avatar,
            cls.update_at,
            cls.deleted_at,
        ).where(cls.login == login).get()

    # Updating the user's password
    @classmethod
    def update_password(cls, login: str, new_password1: str) -> Optional['User']:
        new_password1 = bcrypt.hashpw(new_password1.encode(), bcrypt.gensalt(14))
        user = cls.get(cls.login == login)
        user.password = new_password1
        user.update_at = datetime.datetime.now()
        user.save()
        return user

    # Updating the user's avatar
    @classmethod
    def update_avatar(cls, login, filename) -> Optional['User']:
        user = cls.get(cls.login == login)
        user.avatar = f"img/users/{filename}"
        user.update_at = datetime.datetime.now()
        user.save()
        return user

    class Meta:
        db_table = "Users"
