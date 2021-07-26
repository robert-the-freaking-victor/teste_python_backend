from sqlalchemy.orm import relationship
from orm_database import ORMDatabase
from sqlalchemy.types import PickleType

class Megasena(ORMDatabase.db.Model):
    
	__tablename__ = 'jogo_megasena'
	id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
	user_id = ORMDatabase.db.Column(ORMDatabase.db.Integer, ORMDatabase.db.ForeignKey('users.id'))
	game = ORMDatabase.db.Column(PickleType)
	# num1 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num2 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num3 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num4 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num5 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num6 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=False)
	# num7 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=True)
	# num8 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=True)
	# num9 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=True)
	# num10 = ORMDatabase.db.Column(ORMDatabase.db.Integer, nullable=True)
 
	# def __init__(self, user_id, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
	#  	self.user_id = user_id
	# 	self.num1 = num1
	# 	self.num2 = num2
	# 	self.num3 = num3
	# 	self.num4 = num4
	# 	self.num5 = num5
	# 	self.num6 = num6
	# 	self.num7 = num7
	# 	self.num8 = num8
	# 	self.num9 = num9
	# 	self.num10 = num10
 
	def __init__(self, user_id = None, game = None):
		self.user_id = user_id
		self.game = game
