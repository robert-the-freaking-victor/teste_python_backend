from sqlalchemy.orm import relationship
from orm_database import ORMDatabase
from sqlalchemy.types import PickleType
from datetime import datetime

class Megasena(ORMDatabase.db.Model):
    
	__tablename__ = 'megasena'
	id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
	created_at = ORMDatabase.db.Column(ORMDatabase.db.DateTime, nullable=False)
	user_id = ORMDatabase.db.Column(ORMDatabase.db.Integer, ORMDatabase.db.ForeignKey('users.id'), nullable = False)
	megasena_nums = relationship('MegasenaNum', backref='megasena', cascade='all, delete')
 
	def __init__(self, user_id):
		self.user_id = user_id
		self.created_at = datetime.now()
  
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
	# toDo: commom method between the models. use inheritance
	def create(self):
		ORMDatabase.db.session.add(self)
		ORMDatabase.db.session.commit()