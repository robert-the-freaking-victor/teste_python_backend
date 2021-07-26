from orm_database import ORMDatabase
import datetime
from flask_bcrypt import Bcrypt
from app import App

class User(ORMDatabase.db.Model):
    
    __tablename__= 'users'
    
    __bcrypt = Bcrypt(App.app)
    
    id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
    username = ORMDatabase.db.Column(ORMDatabase.db.String(80), unique=True, nullable=False)
    # email = ORMDatabase.db.Column(ORMDatabase.db.String(120), unique=True, nullable=False)
    password = ORMDatabase.db.Column(ORMDatabase.db.String(100), nullable=False)
    created_at = ORMDatabase.db.Column(ORMDatabase.db.DateTime, nullable=False)
    
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = User.__bcrypt.generate_password_hash(
            password
        ).decode()
        self.created_at = datetime.datetime.now()
        
    def check_password(self, password):
        if User.__bcrypt.check_password_hash(self.password, password):
            return True
        else:
            return False