from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Participation(SerializableObject):

    def __init__(self, event_id: int, person_id: int):
        self.event_id = event_id
        self.person_id = person_id

    @classmethod
    def random(cls):
        event_id = randint(0, 10)
        person_id =randint(0, 10)

        return cls(event_id=event_id, person_id=person_id)

    @classmethod
    def from_json(cls, json):
        event_id = JsonParser.try_get_parameter(json, "event_id")
        person_id = JsonParser.try_get_parameter(json, "person_id")

        return cls(event_id=event_id, person_id=person_id)
