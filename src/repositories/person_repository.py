from src.domain.entities.person import Person
from src.mappers.person_mapper import PersonMapper
from src.repositories.entities.person import Person as DataPerson


class PersonRepository(object):

    def update(self, person: Person):
        return None

    def get_by_id(self, id):
        data_person = DataPerson.select().where(DataPerson.id == id).first()
        return PersonMapper.data_to_domain(data_person)

    def get_all(self):
        data_persons = DataPerson.select()
        return [PersonMapper.data_to_domain(data_person) for data_person in data_persons]
