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
        print("obtido pessoas do evento")

        for person in persons:
            print(person.to_json())
            if not person_repository.get_by_id(person.id):
                person_repository.insert(person)
                print("pessoa adicionada")
            else:
                person_repository.update(person)
                print("pessoa atualizada")

            if not participation_repository.get_by_event_id_and_person_id(event_id, person.id):
                print("adicionando participacao")
                participation = Participation(event_id=int(event_id), person_id=int(person.id))
                participation_repository.insert(participation)
                print("adicionado participacao")
            else:
                print("participacao ja existente")
