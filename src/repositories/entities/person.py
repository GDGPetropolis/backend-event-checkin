from peewee import *
from src.repositories.entities.base_model import BaseModel


class Person(BaseModel):
    id = IntegerField()
    nick = CharField()
    photo = CharField(null=True)
    email = CharField(null=True)
    name = CharField(null=True)
