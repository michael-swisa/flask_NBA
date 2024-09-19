from db import db
from models.player import Player
from requests import request


def get_players(year):
    url_players = rf'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000'
    players_response = request(url=url_players, method='GET')
    return players_response.json()


def load_data_players_from_request(*args):
    players_list = []
    for year in args:
        response = get_players(year)
        players_list.extend(response)
    return players_list


def create_player_to_db(player):
    player_model = Player(
        playerName=player['playerName'],
        team=player['team'],
        position=player['position'],
        points=player['points'],
        season=player['season'],
        games=player['games'],
        twoPercent=player['twoPercent'],
        threePercent=player['threePercent'],
        ATR=player['assists'] / player['turnovers'] if player['turnovers'] > 0 else 0,
        playerId=player['playerId'],
        # PPG_Ratio=player['PPG_Ratio']
    )
    return player_model


def save_player_to_db(player):
    try:
        db.session.add(player)
        db.session.commit()
    except Exception as e:
        print(f'Error while saving player to DB: {e}')
        db.session.rollback()


def load_and_save_players_to_db(years_list):
    players = load_data_players_from_request(*years_list)
    for player in players:
        player_model = create_player_to_db(player)
        save_player_to_db(player_model)
    return


if __name__ == '__main__':
    load_and_save_players_to_db([2022, 2023, 2024])
