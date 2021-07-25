import sys
import os
abs_path = os.path.abspath(os.getcwd())
sys.path.append(abs_path)
from flask import Flask
from dotenv import load_dotenv
from app import App
from src.api.models.user import User
from orm_database import ORMDatabase

load_dotenv(verbose=True)

adm = User(username = "robert", email="rue@hotmail.com", password= "louco")

ORMDatabase.db.session.add(adm)
ORMDatabase.db.session.commit()
print(adm)
App.start_server()