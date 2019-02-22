from src.services.event_synchronizer import EventSynchronizer
from src.services.participation_synchronizer import ParticipationSynchronizer


class EventSynchronizerFacade(object):

    def sync_with_new_data(self, id: int):
        event_synchronizer = EventSynchronizer()
        participation_synchronizar = ParticipationSynchronizer()

        event_synchronizer.sync_with_new_data(id)
        #participation_synchronizar.sync_with_new_data(id)
