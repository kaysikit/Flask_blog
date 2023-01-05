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


    class Meta:
        order_by = "id"
        db_table = "Users"
