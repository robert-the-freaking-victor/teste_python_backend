from orm_database import ORMDatabase
from datetime import datetime
from flask_bcrypt import Bcrypt
from app import App
from sqlalchemy.orm import relationship

class User(ORMDatabase.db.Model):
    
    __tablename__= 'users'
    
    __bcrypt = Bcrypt(App.app)
    
    id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
    username = ORMDatabase.db.Column(ORMDatabase.db.String(80), unique=True, nullable=False)
    # email = ORMDatabase.db.Column(ORMDatabase.db.String(120), unique=True, nullable=False)
    password = ORMDatabase.db.Column(ORMDatabase.db.String(100), nullable=False)
    created_at = ORMDatabase.db.Column(ORMDatabase.db.DateTime, nullable=False)
    megasenas = relationship('Megasena', backref='users', cascade= 'all, delete')
    
    def __init__(self, username = None, password = None):
        self.username = username
        self.set_password(password)
        self.created_at = datetime.now()
        
    def set_password(self, password):
        self.password = User.__bcrypt.generate_password_hash(
            password
        ).decode()
        self.__commit_changes()
    
    def get_password(self):
        return self.password
    
    def set_username(self, username):
        self.username = username
        self.__commit_changes()
        
    def check_password(self, password):
        if User.__bcrypt.check_password_hash(self.password, password):
            return True
        else:
            return False
        
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    # toDo: commom method between the models. use inheritance
    def create(self):
        ORMDatabase.db.session.add(self)
        self.__commit_changes()
        
    def __commit_changes(self):
        ORMDatabase.db.session.commit()
        
    def delete(self):
        ORMDatabase.db.session.delete(self)
        self.__commit_changes()