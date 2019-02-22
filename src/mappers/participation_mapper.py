from src.repositories.entities.participation import Participation as DataParticipation
from src.domain.entities.participation import Participation as DomainParticipation


class ParticipationMapper(object):

    @classmethod
    def data_to_domain(cls, data: DataParticipation):
        return DomainParticipation(event_id=data.event_id, person_id=data.person_id)

    @classmethod
    def domain_to_model(cls, domain: DomainParticipation):
        return DataParticipation(event_id=domain.event_id, person_id=domain.person_id)
