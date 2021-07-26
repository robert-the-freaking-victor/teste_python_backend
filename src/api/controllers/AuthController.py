from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import json
from flask_bcrypt import Bcrypt
import jwt
import os
from src.api.models.users import User
from werkzeug.security import safe_str_cmp
from app import App

auth_bp = Blueprint('Auth', __name__)

class AuthController:
    
    @staticmethod
    @auth_bp.route('/auth',  methods=['POST'])
    def auth():
        bcrypt = Bcrypt(App.app)
        data = request.get_data()
        data = json.loads(data)
        username = data['username']
        password = data['password']
        user = User.query.filter_by(
			username = username
		).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(error='Wrong username or password'), 401
        # primeiro param é a password no banco de dados e o segundo é o valor enviado na requisição
        # bcrypt.check_password_hash(pw_hash, 'secret')

