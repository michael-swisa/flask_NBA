from flask import Blueprint, request, jsonify
from db import db
from models.player import Player
import services.player_service as player_service

bp_player = Blueprint('player', __name__, url_prefix='/api/players')


@bp_player.route('/', methods=['POST'])
def load_and_save_players_to_db():
    years = request.json.get('years')
    player_service.load_and_save_players_to_db(years)
    return jsonify({'message': 'Players loaded and saved to the database'}), 201

@bp_player.route('/', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if not position:
        return jsonify({'error': 'Position is required'}), 400
    if not season:
        players = Player.query.filter_by(position=position).all()
        players_json = [player.to_dict() for player in players]
        return jsonify(players_json)

    players = Player.query.filter_by(position=position, season=season).all()
    players_json = [player.to_dict() for player in players]
    return jsonify(players_json)