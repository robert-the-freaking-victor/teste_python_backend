from flask_sqlalchemy import SQLAlchemy
from app import App
import os

App.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

class ORMDatabase():
    db = SQLAlchemy(App.app)