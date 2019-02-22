from flask import Blueprint

from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler
from src.clients.person_client import PersonClient

person_controller = Blueprint('person', __name__, template_folder='templates')


@person_controller.route('/person', methods=['GET'])
@error_handler
@response_handler
def get():
    person_client = PersonClient()
    return person_client.get_all()
