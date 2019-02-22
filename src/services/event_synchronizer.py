from src.application.mappers.event_mapper import EventMapper
from src.clients.event_client import EventClient
from src.repositories.event_repository import EventRepository


class EventSynchronizer(object):

    def sync_with_new_data(self, id: int):
        event_client = EventClient()
        event_repository = EventRepository()

        event_model = event_client.get_by_id(id)
        event = EventMapper.model_to_domain(event_model)
        event_repository.update(event)
