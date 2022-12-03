from peewee import *
from flask_blog.db.connect_db import db
import os
import datetime


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField(unique=True)
    login = CharField()
    password = CharField()
    date_reg = DateField()

    class Meta:
        order_by = 'id'
        db_table = 'Users'
