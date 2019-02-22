from flask import Flask
from flask_cors import CORS

from src.application.attendance_controller import attendance_controller
from src.application.event_controller import event_controller
from src.application.participant_controller import participant_controller

app = Flask(__name__)
CORS(app)

app.register_blueprint(participant_controller, url_prefix='/api')
app.register_blueprint(event_controller, url_prefix='/api')
app.register_blueprint(attendance_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
