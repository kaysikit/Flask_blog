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
    id = PrimaryKeyField(unique=True)
    login = CharField()
    password = CharField()
    date_reg = DateField(default=datetime.datetime.now)
    avatar = CharField(default="img/default/avatar.png")

    class Meta:
        order_by = "id"
        db_table = "Users"
