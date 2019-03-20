from src.repositories.entities.person import Person as DataPerson
from src.domain.entities.person import Person as DomainPerson
from src.application.models.person_model import PersonModel


class PersonMapper(object):

    @classmethod
    def model_to_domain(cls, model: PersonModel):
        if model:
            return DomainPerson(id=model.id, nick=model.nick, photo=model.photo, email=None, name=None, events=list())

    @classmethod
    def data_to_domain(cls, data: DataPerson):
        if data:
            return DomainPerson(id=data.id, nick=data.nick, photo=data.photo, email=data.email, name=data.name, events=list())

    @classmethod
    def domain_to_model(cls, domain: DomainPerson):
        if domain:
            return DataPerson(id=domain.id, nick=domain.nick, photo=domain.photo, email=domain.email, name=domain.name)
