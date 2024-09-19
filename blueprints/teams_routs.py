from flask import Blueprint, request, jsonify
from db import db
from models.team import Team

bp_team = Blueprint('team', __name__, url_prefix='/api/teams')