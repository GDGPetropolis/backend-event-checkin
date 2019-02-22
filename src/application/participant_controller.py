from flask import Blueprint, request

from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.clients.participant_client import ParticipantClient

person_controller = Blueprint('participant', __name__, template_folder='templates')


@person_controller.route('/participant', methods=['GET'])
@error_handler
@response_handler
def get():
    event_id = request.args.get('event_id')

    if event_id:
        participant_client = ParticipantClient()
        return participant_client.get_all_by_event_id(event_id)
