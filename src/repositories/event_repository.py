from src.mappers.event_mapper import EventMapper
from src.domain.entities.event import Event
from src.mappers.person_mapper import PersonMapper
from src.repositories.entities.event import Event as DataEvent
from src.repositories.entities.participation import Participation as DataParticipation


class EventRepository(object):

    def update(self, event: Event):
        data = DataEvent.update(name=event.name, group_name=event.group_name, link=event.link,
                                local_date=event.local_date, local_time=event.local_time, status=event.status)\
            .where(DataEvent.id == event.id)

        data.execute()
        return self.get_by_id(int(event.id))

    def get_by_id(self, id: int):
        data_event = DataEvent.select().where(DataEvent.id == id).first()

        if data_event:
            domain_event = EventMapper.data_to_domain(data_event)

            data_participations = DataParticipation.select().where(DataParticipation.event == id)
            domain_event.persons = [PersonMapper.data_to_domain(data_participation.person) for data_participation in data_participations]

            return domain_event

    def get_all(self):
        data_events = DataEvent.select()
        domain_events = [EventMapper.data_to_domain(data_event) for data_event in data_events]

        for domain_event in domain_events:
            data_participations = DataParticipation.select().where(DataParticipation.event == domain_event.id)
            domain_event.persons = [PersonMapper.data_to_domain(data_participation.person) for data_participation in
                                    data_participations]

        return domain_events

    def insert(self, event):
        data = DataEvent.create(id=event.id, name=event.name, group_name=event.group_name, link=event.link,
                                local_date=event.local_date, local_time=event.local_time, status=event.status)

        data.save()

        return self.get_by_id(int(event.id))
