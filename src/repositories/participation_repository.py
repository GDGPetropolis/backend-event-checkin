from src.mappers.participation_mapper import ParticipationMapper
from src.repositories.entities.participation import Participation as DataParticipation

class ParticipationRepository(object):

    def add_person_to_event(self, event_id, person_id):
        return None

    def get_by_event_id(self, id):
        data_participations = DataParticipation.select().where(DataParticipation.event == id)
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def get_by_person_id(self, id):
        data_participations = DataParticipation.select().where(DataParticipation.person == id)
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]

    def get_all(self):
        data_participations = DataParticipation.select()
        return [ParticipationMapper.data_to_domain(data_participation) for data_participation in data_participations]
