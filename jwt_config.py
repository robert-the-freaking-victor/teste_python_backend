from app import App
from flask_jwt_extended import JWTManager
from src.api.models.users import User

class JWTConfig:
    jwt = JWTManager(App.app)
    
    # Register a callback function that takes whatever object is passed in as the
	# identity when creating JWTs and converts it to a JSON serializable format.
    @staticmethod
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

 
	# Register a callback function that loades a user from your database whenever
	# a protected route is accessed. This should return any python object on a
	# successful lookup, or None if the lookup failed for any reason (for example
	# if the user has been deleted from the database).
    @staticmethod
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()