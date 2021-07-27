from src.services.scraper import Scraper
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from orm_database import ORMDatabase
import json
from flask_jwt_extended import current_user
from random import randint
from src.api.models.megasena import Megasena
from src.api.models.megasena_nums import MegasenaNum

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
		if request.method == "GET":
			# toDo: method to get all the games from this user
			return MegasenaController.__list_old_games()
		elif request.method == "POST":
			data = request.get_data()
			data = json.loads(data)
			return MegasenaController.__create_random_game(data["unities"])
   
	@staticmethod
	def __create_random_game(nums_to_mark = 6):
		game = []
  
		if nums_to_mark < 6:
			nums_to_mark = 6
		elif nums_to_mark > 10:
			nums_to_mark = 10

		m = Megasena(current_user.id)

		for i in range(nums_to_mark):
			rand_value = randint(1, 60)
			game.append(rand_value)
		
		game.sort()
  
		for i in range(nums_to_mark):
			numMarked = MegasenaNum(m.id, game[i])
			m.megasena_nums.append(numMarked)
	
		m.create()
		return jsonify(game = game, user_id = current_user.id)

	@staticmethod
	def __list_old_games():
		old_games = []
		games = Megasena.query.filter_by(
			user_id = current_user.id
		)
		games = list(games)
		for i in range(len(games)):
			aux = { 'megasena_id': games[i].id , 'nums': [] }
			for j in range(len(games[i].megasena_nums)):
				aux['nums'].append(games[i].megasena_nums[j].num)
			old_games.append(aux)
		return jsonify(old_games=old_games)

	@staticmethod
	@megasena_bp.route('/Megasena/CorrectNumbers', methods=['GET'])
	@jwt_required()
	def correct_numbers():
		nums_result = MegasenaController.__scraper.get_megasena_result()
		print(nums_result)
		game = Megasena.query.filter_by(
			user_id = current_user.id
		).order_by(Megasena.created_at.desc()).first()
		counter = 0
		length = len(nums_result)
		if game:
			for i in range(length):
				for j in range(length):
					print('{0} = {1}'.format(nums_result[i], game.megasena_nums[j].num))
					if nums_result[i] == game.megasena_nums[j].num:
						counter += 1
		return jsonify(correct_numbers=counter)