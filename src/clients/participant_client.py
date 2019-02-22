from src.clients.base_client import BaseClient
from src.domain.entities.participant import Participant


class ParticipantClient(BaseClient):

    def get_all_by_event_id(self, event_id: str):
        return self._get_many("events/" + event_id + "/rsvps?photo-host=public", Participant.from_json)
