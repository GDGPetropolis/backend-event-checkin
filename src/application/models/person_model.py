import uuid
from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class PersonModel(SerializableObject):

    def __init__(self, id: int, name: str, photo: str):
        self.id = id
        self.name = name
        self.photo = photo

    @classmethod
    def random(cls):
        id = randint(0, 10)
        name = str(uuid.uuid4())
        photo = str(uuid.uuid4())

        return cls(id=id, name=name,  photo=photo)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter_with_sub_name(json, "member", "id")
        name = JsonParser.try_get_parameter_with_sub_name(json, "member", "name")
        photo = JsonParser.try_get_parameter_with_two_sub_name(json, "member", "photo", "highres_link")

        return cls(id=id, name=name, photo=photo)
