# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    login = CharField(max_length=255)
    password = CharField(max_length=255)
    date_reg = DateField()
    class Meta:
        table_name = "Users"


