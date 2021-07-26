from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from src.api.models.users import User
import json
from orm_database import ORMDatabase
from flask_jwt_extended import current_user

user_bp = Blueprint('User', __name__)

class UserController:
    
    @staticmethod
    @user_bp.route('/Users', methods=['POST'])
    def create_user():
        data = request.get_data()
        data = json.load(data)
        return UserController.__create(data['username'], data['password'])
            
    @staticmethod
    def __create(username, password):
        newUser = User(username, password)
        ORMDatabase.db.session.add(newUser)
        ORMDatabase.db.session.commit()
        return jsonify(username=username, password=password)