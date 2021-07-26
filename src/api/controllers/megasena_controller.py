from src.services.scraper import Scraper
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

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