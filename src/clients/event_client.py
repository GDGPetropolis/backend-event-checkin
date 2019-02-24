from src.application.models.event_model import EventModel
from src.application.models.person_model import PersonModel
from src.clients.base_client import BaseClient
from src.mappers.event_mapper import EventMapper
from src.mappers.person_mapper import PersonMapper


class EventClient(BaseClient):

    def get_all(self):
        page_index = 1
        event_model = self._get_many("events?photo-host=public&page=" + str(page_index), EventModel.from_json)
        return EventMapper.model_to_domain(event_model)

    def get_by_id(self, id: str):
        event_model = self._get_one("events/" + id + "?photo-host=public", EventModel.from_json)
        return EventMapper.model_to_domain(event_model)

    def get_all_persons_in_event_by_id(self, event_id: int):
        person_models = self._get_many("events/" + event_id + "/rsvps?photo-host=public", PersonModel.from_json)
        return [PersonMapper.model_to_domain(person_model) for person_model in person_models]
