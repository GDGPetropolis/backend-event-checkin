from src.clients.event_client import EventClient
from src.domain.entities.participation import Participation
from src.repositories.participation_repository import ParticipationRepository
from src.repositories.person_repository import PersonRepository


class PersonSynchronizer(object):

    def sync_by_event_id(self, event_id: int):
        event_client = EventClient()
        person_repository = PersonRepository()
        participation_repository = ParticipationRepository()

        persons = event_client.get_all_persons_in_event_by_id(event_id)

        for person in persons:
            if not person_repository.get_by_id(person.id):
                person_repository.insert(person)
            else:
                person_repository.update_without_email_and_name(person)

            if not participation_repository.get_by_event_id_and_person_id(event_id, person.id):
                participation = Participation(event_id=int(event_id), person_id=int(person.id), checkin=False)
                participation_repository.insert(participation)
