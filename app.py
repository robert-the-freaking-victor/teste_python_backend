from flask import Flask
from flask_cors import CORS
import os

class App:
    app = Flask(__name__)
    
    @staticmethod
    def start_server():
        App.app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
        CORS(App.app)
        App.app.run()