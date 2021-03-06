from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class ParticipationRequest(SerializableObject):

    def __init__(self, event_id: int, participant_id: int, checkin: bool):
        self.event_id = event_id
        self.participant_id = participant_id
        self.checkin = checkin

    @classmethod
    def random(cls):
        event_id = randint(0, 10)
        participant_id = randint(0, 10)
        checkin = randint(0, 10) % 2 == 0

        return cls(event_id=event_id, participant_id=participant_id, checkin=checkin)

    @classmethod
    def from_json(cls, json):
        event_id = JsonParser.try_get_parameter(json, "event_id")
        participant_id = JsonParser.try_get_parameter_with_sub_name(json, "participant_id")
        checkin = JsonParser.try_get_parameter(json, "checkin")

        return cls(event_id=event_id, participant_id=participant_id, checkin=checkin)
