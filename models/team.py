from db import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    player_ids = db.relationship('Player', secondary='player_teams', back_populates='teams')
