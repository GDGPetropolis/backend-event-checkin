import uuid
from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Event(SerializableObject):

    def __init__(self, id: int, group_name: str, name: str, status: str, local_date: str, local_time: str,
                 link: str, persons: list):
        self.id = id
        self.group_name = group_name
        self.name = name
        self.status = status
        self.local_date = local_date
        self.local_time = local_time
        self.link = link
        self.persons = persons

    @classmethod
    def random(cls):
        id = randint(0, 10)
        group_name = str(uuid.uuid4())
        name = str(uuid.uuid4())
        status = str(uuid.uuid4())
        local_date = str(uuid.uuid4())
        local_time = str(uuid.uuid4())
        link = str(uuid.uuid4())
        persons = [i for i in range(1, 10)]

        return cls(id=id, group_name=group_name, name=name, status=status, local_date=local_date, local_time=local_time,
                   link=link, persons=persons)

    @classmethod
    def from_json(cls, json):
            id = JsonParser.try_get_parameter(json, "id")
            group_name = JsonParser.try_get_parameter_with_sub_name(json, "group", "name")
            name = JsonParser.try_get_parameter(json, "name")
            status = JsonParser.try_get_parameter(json, "status")
            local_date = JsonParser.try_get_parameter(json, "local_date")
            local_time = JsonParser.try_get_parameter(json, "local_time")
            link = JsonParser.try_get_parameter(json, "link")

            return cls(id=id, group_name=group_name, name=name, status=status, local_date=local_date, local_time=local_time,
                       link=link, persons=list())
