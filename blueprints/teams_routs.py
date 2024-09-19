from flask import Blueprint, request, jsonify
from db import db
from services.teams_service import *

bp_teams = Blueprint('team', __name__)

@bp_teams.route('/', methods=['POST'])
def create_team():
    data = request.get_json()
    return create_team_to_db(data)


@bp_teams.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'team deleted'}), 200


@bp_teams.route('/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    return update_team_in_db(team_id, data)
