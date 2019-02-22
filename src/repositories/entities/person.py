from peewee import *
from src.repositories.entities.base_model import BaseModel


class Person(BaseModel):
    id = IntegerField()
    name = CharField()
    photo = CharField()
    email = CharField()
