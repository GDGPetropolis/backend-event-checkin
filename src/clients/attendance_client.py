from src.clients.base_client import BaseClient
from src.application.models.participant import Participant


class AttendanceClient(BaseClient):

    def get_all_by_event_id(self, event_id: str):
        return self._get_many("events/" + event_id + "/attendance?photo-host=public", Participant.from_json)
