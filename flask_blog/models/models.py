import bcrypt
from peewee import *
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD
import datetime

# Connect with database PostgreSQL
db = PostgresqlDatabase(
    database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)


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
    def new(self, password) -> bool:
        user_exist = True
        try:
            check_user = User.select().where(User.login == self)
            if check_user:
                user_exist = False
        except DoesNotExist as de:
            user_exist = False

        if user_exist:
            row = User(login=self, password=password)
            row.save()
            return True
        return False

    #User authorization
    def autenfication(self, psw) -> bool:
        try:
            check_password = User.get(User.login == self)
            salt = check_password.password.encode()
            if bcrypt.checkpw(psw, salt):
                return True
        finally:
            if db:
                db.close()

        return False

    #Getting a list of all users
    def get_all() -> object:
        return User.select(User.login, User.create_at)

    #
    def get_profile(self: object) -> object:
        return User.select().where(User.login == self).get()

    def update_password(self, new_psw1) -> bool:
        try:
            user = User.get(User.login == self)
            user.password = new_psw1
            user.update_at = datetime.datetime.now()
            user.save()
            return True
        finally:
            if db:
                db.close()

        return False

    def replace_avatar(self, filename) -> bool:
        try:
            user = User.get(User.login == self)
            user.avatar = "img/users/" + filename
            user.update_at = datetime.datetime.now()
            user.save()
            return True
        finally:
            if db:
                db.close()

        return False

    class Meta:
        order_by = "id"
        db_table = "Users"
