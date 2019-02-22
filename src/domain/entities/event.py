from datetime import datetime
from src.infratructure.serializable_object import SerializableObject


class Event(SerializableObject):

    def __init__(self, id: int, group: str, name: str, status: str, date_time: datetime, go_list_count: int, wait_list_count: int, link: str, description: str, how_to_find_us: str):
        self.id = id
        self.group = group
        self.name = name
        self.status = status
        self.datetime = datetime
        self.date_time = date_time
        self.go_list_count = go_list_count
        self.wait_list_count = wait_list_count
        self.link = link
        self.description = description
        self.how_to_find_us = how_to_find_us
