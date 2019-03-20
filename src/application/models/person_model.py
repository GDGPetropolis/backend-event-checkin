import uuid
from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class PersonModel(SerializableObject):

    def __init__(self, id: int, nick: str, photo: str, name: str = None):
        self.id = id
        self.nick = nick
        self.photo = photo
        self.name = name

    @classmethod
    def random(cls):
        id = randint(0, 10)
        nick = str(uuid.uuid4())
        photo = str(uuid.uuid4())
        name = str(uuid.uuid4())

        return cls(id=id, nick=nick, photo=photo, name=name)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter_with_sub_name(json, "member", "id")
        nick = JsonParser.try_get_parameter_with_sub_name(json, "member", "name")
        photo = JsonParser.try_get_parameter_with_two_sub_name(json, "member", "photo", "highres_link")

        return cls(id=id, nick=nick, photo=photo, name=None)
