from peewee import *
from src.repositories.entities.base_model import BaseModel
from src.repositories.entities.event import Event
from src.repositories.entities.person import Person


class Participation(BaseModel):
    event = ForeignKeyField(Event, backref='participation')
    person = ForeignKeyField(Person, backref='participation')

