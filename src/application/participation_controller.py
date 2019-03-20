from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.domain.entities.participation import Participation
from src.repositories.participation_repository import ParticipationRepository

participation_controller = Blueprint('participation', __name__, template_folder='templates')


@participation_controller.route('/participation', methods=['GET'])
@error_handler
@response_handler
def get():
    participation_repository = ParticipationRepository()

    event_id = request.args.get('event_id')
    person_id = request.args.get('person_id')

    if event_id and person_id:
        return participation_repository.get_by_event_id_and_person_id(event_id=event_id, person_id=person_id)
    if event_id:
        return participation_repository.get_by_event_id(event_id)
    elif person_id:
        return participation_repository.get_by_person_id(person_id)

    return participation_repository.get_all()


@participation_controller.route('/participation', methods=['POST'])
@error_handler
@response_handler
def post():
    participation = Participation.from_json(request.get_json())

    if participation:
        participation_repository = ParticipationRepository()
        return participation_repository.set_checkin_by_event_and_person_id(person_id=participation.person_id, event_id=participation.event_id, status=participation.checkin)
