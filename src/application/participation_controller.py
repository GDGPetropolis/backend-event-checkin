from flask import Blueprint, request

from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.clients.participant_client import ParticipantClient
from src.repositories.participation_repository import ParticipationRepository

participation_controller = Blueprint('participation', __name__, template_folder='templates')


@participation_controller.route('/participation/event', methods=['GET'])
@error_handler
@response_handler
def get_event_participations():
    event_id = request.args.get('event_id')

    if event_id:
        participant_repository = ParticipationRepository()
        return participant_repository.get_all_by_event_id(event_id)


@participation_controller.route('/participation/person', methods=['GET'])
@error_handler
@response_handler
def get_person_participations():
    person_id = request.args.get('person_id')

    if person_id:
        participant_repository = ParticipationRepository()
        return participant_repository.get_all_by_person_id(person_id)
