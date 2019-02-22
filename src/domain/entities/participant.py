import uuid
from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Participant(SerializableObject):

    def __init__(self, id: int, name: str, will_go: bool, photo: str):
        self.id = id
        self.name = name
        self.will_go = will_go
        self.photo = photo

    @classmethod
    def random(cls):
        id = randint(0, 10)
        name = str(uuid.uuid4())
        will_go = randint(0, 10) % 2 == 0
        photo = str(uuid.uuid4())

        return cls(id=id, name=name, will_go=will_go, photo=photo)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter_with_sub_name(json, "member", "id")
        name = JsonParser.try_get_parameter_with_sub_name(json, "member", "name")
        will_go = JsonParser.try_get_parameter(json, "response") == "yes"
        photo = JsonParser.try_get_parameter_with_two_sub_name(json, "member", "photo", "highres_link")

        return cls(id=id, name=name, will_go=will_go, photo=photo)
