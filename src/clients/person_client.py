from src.clients.base_client import BaseClient
from src.domain.entities.event import Event


class PersonClient(BaseClient):

    def get_all(self):
        page_index = 1
        return self._get_many("events?photo-host=public&page=" + str(page_index), Event.from_json)
