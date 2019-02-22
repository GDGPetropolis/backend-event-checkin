from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.repositories.participation_repository import ParticipationRepository

participation_controller = Blueprint('participation', __name__, template_folder='templates')


@participation_controller.route('/participation', methods=['POST'])
@error_handler
@response_handler
def post():
    event_id = request.args.get('event_id')
    person_id = request.args.get('person_id')

    if event_id and person_id:
        participation_repository = ParticipationRepository()
        participation_repository.add_person_to_event(event_id, person_id)
