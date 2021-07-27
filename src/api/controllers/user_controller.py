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
    def users_route():
        data = request.get_data()
        data = json.loads(data)
        if request.method == 'POST':
            return UserController.__create(data['username'], data['password'])
        elif request.method == 'PUT':
            return UserController.__update_user(data)
            
    @staticmethod
    def __create(username, password):
        newUser = User(username, password)
        newUser.create()
        return jsonify(username=username, password=newUser.get_password(), id=newUser.id)
    
        
    @staticmethod
    @user_bp.route('/Users/<int:user_id>', methods=['PUT', 'DELETE'])
    @jwt_required()
    def specific_user(user_id):
        if request.method == 'PUT':
            data = request.get_data()
            data = json.loads(data)
            return UserController.__update_user(user_id, data)
        elif request.method == 'DELETE':
            return UserController.__delete_user(user_id)
            
        
    @staticmethod
    def __update_user(user_id, data):
        if user_id == current_user.id:
            if 'username' in data:
                current_user.set_username(data['username'])
            if 'password' in data:
                current_user.set_password(data['password'])
            return jsonify(success='Your user was updated.')
        else:
            return jsonify(error='You only can change your own user.'), 401
    
    @staticmethod
    def __delete_user(user_id):
        if user_id == current_user.id:
            current_user.delete()
            return jsonify(success='User deleted with success.'), 200
        else:
            return jsonify(error='You only can delete your own user.'), 401