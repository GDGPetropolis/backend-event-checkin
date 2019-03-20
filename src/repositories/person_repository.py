from src.domain.entities.person import Person
from src.mappers.person_mapper import PersonMapper
from src.repositories.entities.person import Person as DataPerson


class PersonRepository(object):

    def insert(self, person: Person):
        data = DataPerson.create(id=person.id, nick=person.nick, email=person.email, photo=person.photo, name=person.name)
        data.save()
        return self.get_by_id(int(person.id))

    def update_without_email_and_name(self, person: Person):
        data = DataPerson.update(nick=person.nick, photo=person.photo).where(DataPerson.id == person.id)

        data.execute()
        return self.get_by_id(int(person.id))

    def update_email_and_name(self, id: int, email: str, name: str):
        data = DataPerson.update(email=email, name=name).where(DataPerson.id == id)

        data.execute()
        return self.get_by_id(int(id))

    def get_by_id(self, id: int):
        data_person = DataPerson.select().where(DataPerson.id == id).first()
        return PersonMapper.data_to_domain(data_person)

    def get_all(self):
        data_persons = DataPerson.select()
        return [PersonMapper.data_to_domain(data_person) for data_person in data_persons]
