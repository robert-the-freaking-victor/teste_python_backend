from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from src.api.models.users import User
import json
from orm_database import ORMDatabase

user_bp = Blueprint('User', __name__)

class UserController:
    
    @staticmethod
    @user_bp.route('/Users', methods=['POST, GET'])
    def generalUsers():
        data = request.get_data()
        data = json.load(data)
        if request.method == 'POST':
           return UserController.__create(data['username'], data['password'])
            
    @staticmethod
    def __create(username, password):
        newUser = User(username, password)
        ORMDatabase.db.session.add(newUser)
        ORMDatabase.db.session.commit()
        return jsonify(username=username, password=password)