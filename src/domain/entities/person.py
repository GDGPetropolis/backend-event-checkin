import uuid
from random import randint

from src.domain.entities.event import Event
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Person(SerializableObject):

    def __init__(self, id: int, nick: str, photo: str, email: str = None, name: str = None, events: list = None):
        self.id = id
        self.nick = nick
        self.photo = photo
        self.email = email
        self.name = name
        self.events = events

    @classmethod
    def random(cls):
        id = randint(0, 10)
        nick = str(uuid.uuid4())
        photo = str(uuid.uuid4())
        email = str(uuid.uuid4())
        name = str(uuid.uuid4())
        events = [Event.random() for i in range(0, 10)]

        return cls(id=id, nick=nick, photo=photo, email=email, name=name, events=events)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter(json, "id")
        nick = JsonParser.try_get_parameter(json, "nick")
        photo = JsonParser.try_get_parameter(json, "photo")
        email = JsonParser.try_get_parameter(json, "email")
        name = JsonParser.try_get_parameter(json, "name")

        return cls(id=id, nick=nick, photo=photo, email=email, name=name, events=list())
