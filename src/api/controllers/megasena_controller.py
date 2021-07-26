from src.services.scraper import Scraper
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from orm_database import ORMDatabase
import json
from flask_jwt_extended import current_user
from random import randint
from src.api.models.megasena import Megasena

megasena_bp = Blueprint('GameMegasena', __name__)

class MegasenaController:   
       
	__scraper = Scraper()
 
	@staticmethod
	@megasena_bp.route('/Megasena/Results', methods=["GET"])
	@jwt_required()
	def results():
		"""Get the last result of the game

		Returns:
			array: the nums of the lucky
		"""
		nums_result = MegasenaController.__scraper.get_megasena_result()
		return jsonify(results=nums_result)

	@staticmethod
	@megasena_bp.route('/Megasena', methods=["GET", "POST"])
	@jwt_required()
	def general_megasena():
		data = request.get_data()
		data = json.loads(data)
		if request.method == "GET":
			# toDo: method to get all the games from this user
			return []
		elif request.method == "POST":
			return MegasenaController.__create_random_game(data["unities"])
   
	@staticmethod
	def __create_random_game(nums_to_mark = 6):
		game = []
		for i in range(nums_to_mark):
			game.append(randint(1, 60))
   
		m = Megasena(current_user.id, game)
		ORMDatabase.db.session.add(m)
		ORMDatabase.db.session.commit()
		return jsonify(game=game, user_id = current_user.id)
