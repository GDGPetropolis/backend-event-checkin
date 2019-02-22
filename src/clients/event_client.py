from src.application.models.participant_model import ParticipantModel
from src.clients.base_client import BaseClient
from src.domain.entities.event import Event


class EventClient(BaseClient):

    def get_all(self):
        page_index = 1
        return self._get_many("events?photo-host=public&page=" + str(page_index), Event.from_json)

    def get_by_id(self, id: str):
        return self._get_one("events/" + id + "?photo-host=public", Event.from_json)

    def get_all_participant_by_id(self, event_id: int):
        return self._get_many("events/" + event_id + "/rsvps?photo-host=public", ParticipantModel.from_json)
