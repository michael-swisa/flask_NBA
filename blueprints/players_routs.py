from flask import Blueprint, request, jsonify
from db import db
from models.player import Player
import services.player_service as player_service

bp_player = Blueprint('player', __name__, url_prefix='/players')


@bp_player.route('/', methods=['POST'])
def load_and_save_players_to_db():
    years = request.json.get('years')
    player_service.load_and_save_players_to_db(years)
    return jsonify({'message': 'Players loaded and saved to the database'}), 201
