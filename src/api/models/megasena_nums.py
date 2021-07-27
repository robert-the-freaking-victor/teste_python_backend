from orm_database import ORMDatabase
from sqlalchemy.orm import relationship

class MegasenaNum(ORMDatabase.db.Model):
	__table_name__ = 'megasenanums'
	id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
	megasena_id = ORMDatabase.db.Column(ORMDatabase.db.Integer, ORMDatabase.db.ForeignKey('megasena.id'), nullable = False)
	num = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable = False)
 
	def __init__(self, megasena_id = None, num = None):
		self.megasena_id = megasena_id
		self.num = num
  
	# toDo: commom method between the models. use inheritance
	def create(self):
		ORMDatabase.db.session.add(self)
		ORMDatabase.db.session.commit()