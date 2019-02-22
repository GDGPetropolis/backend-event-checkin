from src.repositories.entities.person import Person as DataPerson
from src.domain.entities.person import Person as DomainPerson


class PersonMapper(object):

    @classmethod
    def data_to_domain(cls, data: DataPerson):
        return DomainPerson(id=data.id, name=data.name, photo=data.photo, email=data.email, events=list())

    @classmethod
    def domain_to_model(cls, domain: DomainPerson):
        return DataPerson(id=domain.id, name=domain.name, photo=domain.photo, email=domain.email)
