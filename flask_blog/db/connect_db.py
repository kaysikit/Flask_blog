from peewee import *
from config import user, password, db_name, host

# Connect with database PostgreSQL
db = PostgresqlDatabase(database=db_name, user=user, password=password, host=host)
