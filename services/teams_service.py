from sqlalchemy.exc import IntegrityError

from db import db
from models.team import Team
from flask import jsonify
from models.player import Player

def save_team(team):
    print(team.to_dict())
    try:
        db.session.add(team)
        db.session.commit()
        return jsonify({'message': 'Team created successfully', 'team_id': team.id}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({
                           'message': 'The name of the player already exists or one of the players is already played '
                                      'in another game'}), 409

    except Exception as e:
        print(f'Error while creating team: {e}')
        db.session.rollback()
        return jsonify({'message': 'Error while creating team'}), 500



def create_team_to_db(data):
    if not data['team_name'] or not data['player_ids']:
        return jsonify({'message': 'Missing team name or player ids'}), 400
    teme_name = data['team_name']
    player_ids = data['player_ids']
    if len(player_ids) != 5:
        return jsonify({'message': 'Team must have exactly 5 players'}), 400
    team = create_team(data)
    if not team:
        return jsonify({'message': 'Player not found Team must have exactly 5 players'}), 400
    return save_team(team)


def create_team(data):
    position_dict = {}
    for playerId in data['player_ids']:
        player = Player.query.filter_by(playerId=playerId).first()
        if not player:
            return None
        position = player.position
        position_dict[position] = playerId
    if len(position_dict) != 5:
        return None
    team = Team(
        team_name=data['team_name'],
        C=position_dict['C'],
        PF=position_dict['PF'],
        SF=position_dict['SF'],
        SG=position_dict['SG'],
        PG=position_dict['PG']
    )
    return team



def update_team_in_db(team_id, data):
    team = Team.query.get_or_404(team_id)
    # if data['team_name']:
    #     team.team_name = data['team_name']
    if not data['player_ids']:
        return jsonify({'message': 'Missing player ids'}), 400
    player_ids = data['player_ids']
    if len(player_ids) != 5:
        return jsonify({'message': 'Team must have exactly 5 players'}), 400
    team_update = create_team(data)
    if not team_update:
        return jsonify({'message': 'Player not found Team must have exactly 5 players'}), 400
    return update_team(team_update, team)


def update_team(team_update, team):
    if not team:
        return jsonify({'message': 'Missing team id'}), 400
    try:
        team.team_name = team_update.team_name or team.team_name
        team.C = team_update.C
        team.PF = team_update.PF
        team.SF = team_update.SF
        team.SG = team_update.SG
        team.PG = team_update.PG
        db.session.commit()
        return jsonify({'message': 'Team updated successfully', 'team_id': team.id}), 200
    except Exception as e:
        print(f'Error while updating team: {e}')
        db.session.rollback()
        return jsonify({'message': 'Error while updating team'}), 500

