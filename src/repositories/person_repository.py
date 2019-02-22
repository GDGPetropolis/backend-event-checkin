from src.domain.entities.person import Person
from src.repositories.entities.person import Person as DataPerson

class PersonRepository(object):

    def update(self, person: Person):
        return None

    def get_by_id(self, id):
        data_event = DataPerson.select().where(DataPerson.id == id).first()
        return PersonMapper.data_to_domain(data_event)

    def get_all(self):
        return None
