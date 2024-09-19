from flask import Flask
from blueprints.teams_routs import bp_teams
from blueprints.players_routs import bp_player
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()

app.register_blueprint(bp_teams, url_prefix='/api/teams')
app.register_blueprint(bp_player, url_prefix='/api/players')




if __name__ == '__main__':
    app.run(debug=True)
