from src.services.event_synchronizer import EventSynchronizer
from src.services.person_synchronizer import PersonSynchronizer
from src.repositories.event_repository import EventRepository


class EventSynchronizerFacade(object):

    def sync_one_by_id(self, id: int):
        event_synchronizer = EventSynchronizer()
        participation_synchronizer = PersonSynchronizer()
        event_repository = EventRepository()

        event_synchronizer.sync_one_by_id(id)
        print("evento sincronizado")

        participation_synchronizer.sync_by_event_id(id)
        print("pessoas e participacoes atualizadas")

        return event_repository.get_by_id(id)
