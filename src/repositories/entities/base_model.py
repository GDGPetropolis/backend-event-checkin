from peewee import *
import os

try:
    database = os.environ['DATABASE']
    user = os.environ['DATABASE_USER']
    password = os.environ['DATABASE_USER_PASSWORD']
    host = os.environ['DATABASE_HOST']
    port = int(os.environ['DATABASE_PORT'])

    print("Using Docker Environment")

except:
    database = "GdgDatabase"
    user = "GdgUser"
    password = "GdgPassword"
    host = "localhost"
    port = 3306

    print("Using Local Environment")

mysql_db = MySQLDatabase(database, user=user, password=password, host=host, port=port)


class BaseModel(Model):
    class Meta:
        database = mysql_db
