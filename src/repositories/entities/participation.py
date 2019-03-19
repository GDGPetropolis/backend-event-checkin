from peewee import *
from src.repositories.entities.base_model import BaseModel
from src.repositories.entities.event import Event
from src.repositories.entities.person import Person


class Participation(BaseModel):
    id = IntegerField()
    checkin = BooleanField(default=False)
    event = ForeignKeyField(Event, backref='participations')
    person = ForeignKeyField(Person, backref='participations')


