from flask import Flask
from blueprints.teams_routs import bp_team
from blueprints.players_routs import bp_player
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bp_team, url_prefix='/users')
app.register_blueprint(bp_player, url_prefix='/players')




if __name__ == '__main__':
    app.run(debug=True)
