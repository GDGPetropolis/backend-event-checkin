from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_handler import response_handler

attendance_controller = Blueprint('attendance', __name__, template_folder='templates')


@attendance_controller.route('/attendance', methods=['GET'])
@error_handler
@response_handler
def get():
    event_id = request.args.get('event_id')

    if event_id:
        attendance_client = AttendanceClient()
        return attendance_client.get_all_by_event_id(event_id)




