# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class BaseModel(peewee.Model):
    class Meta:
        table_name = "basemodel"


@snapshot.append
class User(peewee.Model):
    login = TextField()
    password = CharField(max_length=255)
    create_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = TextField(null=True)
    avatar = CharField(default="img/default/avatar.png", max_length=255)

    class Meta:
        table_name = "Users"


def forward(old_orm, new_orm):
    user = new_orm["user"]
    old_user = old_orm["user"]
    return [
        # Apply default value datetime.datetime(2023, 1, 5, 21, 52, 52, 755612) to the field user.update_at,
        user.update(
            {user.update_at: datetime.datetime(2023, 1, 5, 21, 52, 52, 755612)}
        ).where(user.update_at.is_null(True)),
        # Apply default value datetime.datetime(2023, 1, 5, 21, 52, 52, 755612) to the field user.create_at,
        user.update(
            {user.create_at: datetime.datetime(2023, 1, 5, 21, 52, 52, 755612)}
        ).where(user.create_at.is_null(True)),
        # Don't know how to do the conversion correctly, use the naive,
        user.update({user.login: old_user.login}).where(old_user.login.is_null(False)),
    ]


def backward(old_orm, new_orm):
    user = new_orm["user"]
    old_user = old_orm["user"]
    return [
        # Apply default value datetime.datetime(2023, 1, 5, 21, 52, 52, 755612) to the field user.date_reg,
        user.update(
            {user.date_reg: datetime.datetime(2023, 1, 5, 21, 52, 52, 755612)}
        ).where(user.date_reg.is_null(True)),
        # Convert datatype of the field user.login: TEXT -> VARCHAR(255),
        user.update({user.login: old_user.login.cast("VARCHAR")}).where(
            old_user.login.is_null(False)
        ),
    ]
