from src.application.models.event_model import EventModel
from src.repositories.entities.event import Event as DataEvent
from src.domain.entities.event import Event


class EventMapper(object):

    @classmethod
    def model_to_domain(cls, model: EventModel):
        return Event(id=model.id, group_name=model.group_name, name=model.name, status=model.status, local_date=model.local_date,
                     local_time=model.local_time, link=model.link, persons=list())

    @classmethod
    def data_to_domain(cls, data: DataEvent):
        return Event(id=data.id, group_name=data.group_name, name=data.name, status=data.status, local_date=data.local_date,
                     local_time=data.local_time, link=data.link, persons=list())

    @classmethod
    def domain_to_model(cls, domain: Event):
        return EventModel(id=domain.id, group_name=domain.group, name=domain.name, status=domain.status,
                          local_date=domain.local_date, local_time=domain.local_time, link=domain.link,
                          go_list_count=0, wait_list_count=0)
