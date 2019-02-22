from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.clients.event_client import EventClient

event_controller = Blueprint('event', __name__, template_folder='templates')


@event_controller.route('/event', methods=['GET'])
@error_handler
@response_handler
def get():
    event_client = EventClient()

    id = request.args.get('id')

    if id:
        event_client = EventClient()
        return event_client.get_by_id(id)

    return event_client.get_all()



