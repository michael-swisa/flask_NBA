import my_request
from itertools import groupby
import files


def load_data_players_from_request(*args):
    players = []
    for year in args:
        response = my_request.get_players(year)
        players.extend(response)
    return players

def sorted_json_players(players):
    sorted_players = sorted(players, key=lambda player: player['playerName'])
    return sorted_players
def group_players_by_name(players):
    grouped_players = {}

def group_players_by_name(players):
    grouped_players = {}
    for key, value in groupby(players, key=lambda player: player['playerName']):
        grouped_players[key] = list(value)
    return grouped_players

def save_to_json(data, filename):
    files.write_json(filename, data)

if __name__ == '__main__':
    players = load_data_players_from_request(2022, 2023, 2024)
    players_sorted = sorted_json_players(players)
    players_grouped = group_players_by_name(players_sorted)
    save_to_json(players_grouped, 'players_grouped.json')