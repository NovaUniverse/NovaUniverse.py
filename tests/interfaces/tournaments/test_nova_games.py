import requests
from ... import NovaGames

from dataclasses import asdict
from typing import Dict

data_from_raw_request = requests.get(url="https://api.novauniverse.net/v1/tournaments/nova_games/result").json()

def test_nova_games_get_all():
    data_from_wrapper = [nova_games.data for nova_games in NovaGames().get_all()]

    assert data_from_raw_request == data_from_wrapper

def test_nova_games_get_latest():
    data_from_wrapper = NovaGames().get_latest().data

    assert data_from_raw_request[-1] == data_from_wrapper

def test_nova_games_get_top_players():
    data_from_wrapper = [asdict(player) for player in NovaGames().get_top_players()]
    
    count = 0
    for player in data_from_wrapper:
        del player["data"]; del player["logger"]; del player["name"]
        data_from_wrapper[count] = player

        count += 1

    players: Dict[str, dict] = {}

    for player in [player for nova_games in data_from_raw_request for player in nova_games["players"]]:
        if player["uuid"] in players:
            players[player["uuid"]]["score"] = player["score"] + players[player["uuid"]]["score"]
            players[player["uuid"]]["kills"] = player["kills"] + players[player["uuid"]]["kills"]
        else:
            player["team_number"] = None; player["uid"] = None # We null these properties as they are irrelevant and are different in every tournament.
            players[player["uuid"]] = player

    _data_from_raw_request = [item[1] for item in sorted(players.items(), key=lambda x: x[1]["score"], reverse=True)[:15]]

    assert _data_from_raw_request == data_from_wrapper