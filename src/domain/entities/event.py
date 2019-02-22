import uuid
from random import randint
from src.infratructure.json_parser import JsonParser
from src.infratructure.serializable_object import SerializableObject


class Event(SerializableObject):

    def __init__(self, id: int, group: str, name: str, status: str, local_date: str, local_time: str,
                 go_list_count: int, wait_list_count: int, link: str, description: str, how_to_find_us: str):
        self.id = id
        self.group = group
        self.name = name
        self.status = status
        self.local_date = local_date
        self.local_time = local_time
        self.go_list_count = go_list_count
        self.wait_list_count = wait_list_count
        self.link = link
        self.description = description
        self.how_to_find_us = how_to_find_us

    @classmethod
    def random(cls):
        id = randint(0, 10)
        group = str(uuid.uuid4())
        name = str(uuid.uuid4())
        status = str(uuid.uuid4())
        local_date = str(uuid.uuid4())
        local_time = str(uuid.uuid4())
        go_list_count = randint(0, 10)
        wait_list_count = randint(0, 10)
        link = str(uuid.uuid4())
        description = str(uuid.uuid4())
        how_to_find_us = str(uuid.uuid4())

        return cls(id=id, group=group, name=name, status=status, local_date=local_date, local_time=local_time,
                   go_list_count=go_list_count, wait_list_count=wait_list_count, link=link, description=description,
                   how_to_find_us=how_to_find_us)

    @classmethod
    def from_json(cls, json):
            id = JsonParser.try_get_parameter(json, "id")
            group = JsonParser.try_get_parameter_with_sub_name(json, "group", "name")
            name = JsonParser.try_get_parameter(json, "name")
            status = JsonParser.try_get_parameter(json, "status")
            local_date = JsonParser.try_get_parameter(json, "local_date")
            local_time = JsonParser.try_get_parameter(json, "local_time")
            go_list_count = JsonParser.try_get_parameter(json, "yes_rsvp_count")
            wait_list_count = JsonParser.try_get_parameter(json, "waitlist_count")
            link = JsonParser.try_get_parameter(json, "link")
            description = JsonParser.try_get_parameter(json, "description")
            how_to_find_us = JsonParser.try_get_parameter(json, "how_to_find_us")

            return cls(id=id, group=group, name=name, status=status, local_date=local_date, local_time=local_time,
                       go_list_count=go_list_count, wait_list_count=wait_list_count, link=link, description=description,
                       how_to_find_us=how_to_find_us)
