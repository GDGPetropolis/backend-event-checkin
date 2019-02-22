from src.application.mappers.event_mapper import EventMapper
from src.domain.entities.event import Event
from src.repositories.entities.event import Event as DataEvent


class EventRepository(object):

    def update(self, event: Event):
        print(event.to_json())

    def get_by_id(self, id):
        data_event = DataEvent.select().where(DataEvent.id == id).first()
        return EventMapper.data_to_domain(data_event)

    def get_all(self):
        data_events = DataEvent.select()
        return [EventMapper.data_to_domain(data_event) for data_event in data_events]
