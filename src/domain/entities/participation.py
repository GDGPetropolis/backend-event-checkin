from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Participation(SerializableObject):

    def __init__(self, event_id: int, person_id: int, checkin: bool, id: int = None):
        self.id = id
        self.event_id = event_id
        self.person_id = person_id
        self.checkin = checkin

    @classmethod
    def random(cls):
        id = randint(0, 10)
        event_id = randint(0, 10)
        person_id = randint(0, 10)
        checkin = randint(0, 10) % 2 == 0

        return cls(id=id, event_id=event_id, person_id=person_id, checkin=checkin)

    @classmethod
    def from_json(cls, json):
        id = JsonParser.try_get_parameter(json, "id")
        event_id = JsonParser.try_get_parameter(json, "event_id")
        person_id = JsonParser.try_get_parameter(json, "person_id")
        checkin = JsonParser.try_get_parameter(json, "checkin")

        return cls(id=id, event_id=event_id, person_id=person_id, checkin=checkin)
