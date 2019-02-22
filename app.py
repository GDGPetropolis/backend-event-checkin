from flask import Flask
from flask_cors import CORS
from src.application.person_controller import person_controller

app = Flask(__name__)
CORS(app)

app.register_blueprint(person_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
