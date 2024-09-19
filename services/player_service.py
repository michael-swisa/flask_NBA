import my_request
import files


def load_data_players(*args):
    players = []
    for year in args:
        response = my_request.get_players(year)
        players.extend(response)
    files.write_json(f'players.json', players)


if __name__ == '__main__':
    load_data_players(2022, 2023, 2024)