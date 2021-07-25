from flask import Flask
from flask_cors import CORS

class App:
    app = Flask(__name__)
    
    @staticmethod
    def start_server():
        App.app.run()
        CORS(App.app)
    