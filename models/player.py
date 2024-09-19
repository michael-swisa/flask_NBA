from db import db

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    seasons = db.relationship('Season', secondary='player_seasons', back_populates='players')
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    twoPercent = db.Column(db.Float, nullable=False)
    threePercent = db.Column(db.Float, nullable=False)
    ATR = db.Column(db.Float, nullable=False)
    PPG_Ratio = db.Column(db.Float, nullable=False)