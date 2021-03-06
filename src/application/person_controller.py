from flask import Blueprint, request

from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.domain.entities.person import Person
from src.repositories.person_repository import PersonRepository
from src.services.person_synchronizer import PersonSynchronizer

person_controller = Blueprint('person', __name__, template_folder='templates')


@person_controller.route('/person', methods=['GET'])
@error_handler
@response_handler
def get():
    person_repository = PersonRepository()

    id = request.args.get('id')

    if id:
        return person_repository.get_by_id(id)

    return person_repository.get_all()


@person_controller.route('/person', methods=['PUT'])
@error_handler
@response_handler
def patch():
    person = Person.from_json(request.get_json())

    if person:
        person_repository = PersonRepository()
        data = person_repository.update_email_and_name(person.id, person.email, person.name)
        return data


@person_controller.route('/person/sync', methods=['POST'])
def post():
    id = request.args.get('id')

    if id:
        person_synchronizer = PersonSynchronizer()
        person_synchronizer.sync_with_new_data(id)

    return "sync"


