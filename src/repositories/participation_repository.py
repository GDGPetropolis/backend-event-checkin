from src.mappers.participation_mapper import ParticipationMapper
from src.repositories.entities.participation import Participation as DataParticipation
from src.domain.entities.participation import Participation as DomainParticipation


class ParticipationRepository(object):

    def get_by_event_id(self, event_id: int):
        data_participations = DataParticipation.select().where(DataParticipation.event == event_id)
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def get_by_person_id(self, person_id):
        data_participations = DataParticipation.select().where(DataParticipation.person == person_id)
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def get_by_event_id_and_person_id(self, event_id: int, person_id: int):
        data_participations = DataParticipation.select().where(DataParticipation.person == person_id).where(DataParticipation.event == event_id)
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def get_all(self):
        data_participations = DataParticipation.select()
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def insert(self, domain: DomainParticipation):
        data = DataParticipation.create(event=domain.event_id, person=domain.person_id)
        data.save()

        return self.get_by_event_id_and_person_id(event_id=int(domain.event_id), person_id=int(domain.person_id))
