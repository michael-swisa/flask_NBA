from db import db

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(100), nullable=True)
    team = db.Column(db.String(100), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    season = db.Column(db.String(100), nullable=True)
    points = db.Column(db.Integer, nullable=True)
    games = db.Column(db.Integer, nullable=True)
    twoPercent = db.Column(db.Float, nullable=True)
    threePercent = db.Column(db.Float, nullable=True)
    ATR = db.Column(db.Float, nullable=True)
    playerId = db.Column(db.String(100), nullable=True)
    PPG_Ratio = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            'playerName': self.playerName,
            'team': self.team,
            'position': self.position,
            'season': self.season,
            'points': self.points,
            'games': self.games,
            'twoPercent': self.twoPercent,
            'threePercent': self.threePercent,
            'ATR': self.ATR,
            'PPG_Ratio': self.PPG_Ratio
        }