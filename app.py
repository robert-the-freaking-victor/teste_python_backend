from flask import Flask
from flask_cors import CORS
import os
from datetime import timedelta

class App:
    app = Flask(__name__)
    
    @staticmethod
    def start_server():
        App.app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
        token_expires = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
        App.app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(token_expires)
        CORS(App.app)
        App.app.run()