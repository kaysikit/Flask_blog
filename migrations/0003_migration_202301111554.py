# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    login = TextField()
    password = CharField(max_length=255)
    create_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = TextField(null=True)
    avatar = CharField(default='img/default/avatar.png', max_length=255)
    class Meta:
        table_name = "Users"


