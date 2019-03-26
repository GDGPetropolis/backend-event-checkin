from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.repositories.event_repository import EventRepository
from src.services.event_certificate_generator import EventCertificateGenerator
from src.services.event_synchronizer_facade import EventSynchronizerFacade

event_controller = Blueprint('event', __name__, template_folder='templates')


@event_controller.route('/event', methods=['GET'])
@error_handler
@response_handler
def get():
    event_repository = EventRepository()

    id = request.args.get('id')

    if id:
        return event_repository.get_by_id(id)

    return event_repository.get_all()


@event_controller.route('/event/sync', methods=['POST'])
@error_handler
@response_handler
def post():
    event_synchronizer = EventSynchronizerFacade()

    id = request.args.get('id')

    if id:
        return event_synchronizer.sync_one_by_id(id)
    else:
        return event_synchronizer.sync_all()


@event_controller.route('/event/gen', methods=['POST'])
@error_handler
@response_handler
def gen():
    id = request.args.get('id')

    if id:
        certificate_generator = EventCertificateGenerator()
        certificate_generator.generate_by_event_id(event_id=id)

