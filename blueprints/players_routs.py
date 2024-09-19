from flask import Blueprint, request, jsonify
from db import db
from models.player import Player

bp_player = Blueprint('player', __name__, url_prefix='/players')