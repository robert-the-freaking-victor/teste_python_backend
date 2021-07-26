import sys
import os
abs_path = os.path.abspath(os.getcwd())
sys.path.append(abs_path)
from dotenv import load_dotenv
load_dotenv(verbose=True)
from flask import Flask
from jwt_config import JWTConfig
from app import App
from src.api.models.users import User
from orm_database import ORMDatabase
from src.api.controllers.auth_controller import auth_bp
from src.api.controllers.megasena_controller import megasena_bp
from src.services.scraper import Scraper

ORMDatabase.db.create_all()

App.app.register_blueprint(auth_bp)
App.app.register_blueprint(megasena_bp)
App.start_server()