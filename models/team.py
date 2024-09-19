from db import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    C = db.Column(db.String(100), nullable=False, unique=True)
    PF = db.Column(db.String(100), nullable=False, unique=True)
    SF = db.Column(db.String(100), nullable=False, unique=True)
    SG = db.Column(db.String(100), nullable=False, unique=True)
    PG = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'team_name': self.team_name,
            'C': self.C,
            'PF': self.PF,
            'SF': self.SF,
            'SG': self.SG,
            'PG': self.PG
        }