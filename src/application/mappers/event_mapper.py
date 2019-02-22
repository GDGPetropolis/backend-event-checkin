from src.application.models.event_model import EventModel
from src.domain.entities.event import Event


class EventMapper(object):

    @classmethod
    def model_to_domain(cls, model: EventModel):
        return Event(id=model.id, group=model.group, name=model.name, status=model.status, local_date=model.local_date,
                     local_time=model.local_time, link=model.link, persons=list())

    @classmethod
    def domain_to_model(cls, domain: Event):
        return EventModel(id=domain.id, group=domain.group, name=domain.name, status=domain.status,
                          local_date=domain.local_date, local_time=domain.local_time, link=domain.link,
                          go_list_count=0, wait_list_count=0)
