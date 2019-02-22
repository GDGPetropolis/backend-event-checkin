from flask import Blueprint

from src.application.filters.error_handler import error_handler
from src.application.filters.response_data_validator import has_valid_data_in_response
from src.clients.person_client import PersonClient

person_controller = Blueprint('person', __name__, template_folder='templates')


@person_controller.route('/person', methods=['GET'])
#@error_handler
#@has_valid_data_in_response
def get():
    person_client = PersonClient("api.meetup.com", "GDGPetropolis", "...")

    person_client.get_all()
    return "ok"
