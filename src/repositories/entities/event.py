from peewee import *
from src.repositories.entities.base_model import BaseModel


class Event(BaseModel):
    id = IntegerField()
    name = CharField()
    group_name = CharField()
    link = CharField()
    local_date = CharField()
    local_time = CharField()
    status = CharField()
