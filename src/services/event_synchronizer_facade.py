from src.clients.event_client import EventClient
from src.services.event_synchronizer import EventSynchronizer
from src.services.person_synchronizer import PersonSynchronizer
from src.repositories.event_repository import EventRepository


class EventSynchronizerFacade(object):

    def sync_one_by_id(self, id: int):
        event_synchronizer = EventSynchronizer()
        participation_synchronizer = PersonSynchronizer()
        event_repository = EventRepository()

        event_synchronizer.sync_one_by_id(id)

        participation_synchronizer.sync_by_event_id(id)

        return event_repository.get_by_id(id)

    def sync_all(self):
        event_client = EventClient()
        event_repository = EventRepository()
        events = event_client.get_all()

        for event in events:
            if event_repository.get_by_id(event.id):
                self.sync_one_by_id(event.id)
            else:
                event_repository.insert(event)
                self.sync_one_by_id(event.id)
