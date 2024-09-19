from flask import Blueprint, request, jsonify
from db import db
from services.teams_service import *

bp_teams = Blueprint('team', __name__)

@bp_teams.route('/', methods=['POST'])
def create_team():
    data = request.get_json()
    return create_team_to_db(data)