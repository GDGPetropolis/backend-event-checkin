from src.repositories.entities.participation import Participation as DataParticipation
from src.domain.entities.participation import Participation as DomainParticipation


class ParticipationMapper(object):

    @classmethod
    def data_to_domain(cls, data: DataParticipation):
        if data:
            return DomainParticipation(id=data.id, event_id=data.event_id, person_id=data.person_id)

    @classmethod
    def domain_to_model(cls, domain: DomainParticipation):
        if domain:
            return DataParticipation(id=domain.id, event_id=domain.event_id, person_id=domain.person_id)
