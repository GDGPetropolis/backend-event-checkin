import uuid
from random import randint

from src.domain.entities.event import Event
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Person(SerializableObject):

    def __init__(self, id: int, name: str, photo: str, email: str, events: list):
        self.id = id
        self.name = name
        self.photo = photo
        self.email = email
        self.events = events

    @classmethod
    def random(cls):
        id = randint(0, 10)
        name = str(uuid.uuid4())
        photo = str(uuid.uuid4())
        email = str(uuid.uuid4())
        events = [Event.random() for i in range(0, 10)]

        return cls(id=id, name=name, photo=photo, email=email, events=events)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter(json, "id")
        name = JsonParser.try_get_parameter(json, "name")
        photo = JsonParser.try_get_parameter(json, "photo")
        email = JsonParser.try_get_parameter(json, "email")

        return cls(id=id, name=name, photo=photo, email=email, events=list())
