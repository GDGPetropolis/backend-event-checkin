import abc
import json


class SerializableObject(metaclass=abc.ABCMeta):

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @abc.abstractclassmethod
    def from_json(cls, json):
        pass
