from db import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    C = db.Column(db.String(100), nullable=False)
    PF = db.Column(db.String(100), nullable=False)
    SF = db.Column(db.String(100), nullable=False)
    SG = db.Column(db.String(100), nullable=False)
    PG = db.Column(db.String(100), nullable=False)
