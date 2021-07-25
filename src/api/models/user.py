from orm_database import ORMDatabase

class User(ORMDatabase.db.Model):
    id = ORMDatabase.db.Column(ORMDatabase.db.Integer, primary_key=True)
    username = ORMDatabase.db.Column(ORMDatabase.db.String(80), unique=True, nullable=False)
    email = ORMDatabase.db.Column(ORMDatabase.db.String(120), unique=True, nullable=False)
    password = ORMDatabase.db.Column(ORMDatabase.db.String(100))