from flask_sqlalchemy import SQLAlchemy
from app import App
import os

App.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
App.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class ORMDatabase():
    db = SQLAlchemy(App.app)