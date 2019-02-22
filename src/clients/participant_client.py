from src.clients.base_client import BaseClient
from src.application.models.participant_model import ParticipantModel


class ParticipantClient(BaseClient):

    def get_all_by_event_id(self, event_id: int):
        return self._get_many("events/" + event_id + "/rsvps?photo-host=public", ParticipantModel.from_json)
