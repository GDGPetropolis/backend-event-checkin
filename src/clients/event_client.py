from src.clients.base_client import BaseClient
from src.domain.entities.event import Event


class EventClient(BaseClient):

    def get_all(self):
        page_index = 1

        events = self.get("events?photo-host=public&page=" + str(page_index), Event.from_json)

        for event in events:
            print(event.to_json())
