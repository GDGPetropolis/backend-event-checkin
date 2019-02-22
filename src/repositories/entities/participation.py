from peewee import *
from src.repositories.entities.base_model import BaseModel
from src.repositories.entities.event import Event
from src.repositories.entities.person import Person


class ParticipationCompositeKey(BaseModel):
    class Meta:
        primary_key = CompositeKey('event_id', 'person_id')


class Participation(ParticipationCompositeKey):
    event = ForeignKeyField(Event, backref='participations')
    person = ForeignKeyField(Person, backref='participations')

