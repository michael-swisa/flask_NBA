from requests import request


def get_players(year):
    url_players = rf'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000'
    players_response = request(url=url_players, method='GET')
    return players_response.json()


