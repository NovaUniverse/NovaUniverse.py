import requests
from .. import MCF

from dataclasses import asdict
from typing import List, Dict

def test_mcf_get_all():
    data_from_wrapper = [mcf.data for mcf in MCF().get_all()]
    data_from_raw_request = requests.get(url="https://api.novauniverse.net/v1/tournaments/mcf/result").json()

    assert data_from_raw_request == data_from_wrapper

def test_mcf_get_latest():
    data_from_wrapper = MCF().get_latest().data
    data_from_raw_request = requests.get(url="https://api.novauniverse.net/v1/tournaments/mcf/result").json()[-1]

    assert data_from_raw_request == data_from_wrapper

def test_mcf_get_top_players():
    data_from_wrapper = [asdict(player) for player in MCF().get_top_players()]
    
    count = 0
    for player in data_from_wrapper:
        del player["data"]; del player["logger"]; del player["name"]
        data_from_wrapper[count] = player

        count += 1

    data_from_raw_request: List[dict] = requests.get(url="https://api.novauniverse.net/v1/tournaments/mcf/result").json()

    players: Dict[str, dict] = {}

    for player in [player for mcf in data_from_raw_request for player in mcf["players"]]:
        if player["uuid"] in players:
            players[player["uuid"]]["score"] = player["score"] + players[player["uuid"]]["score"]
            players[player["uuid"]]["kills"] = player["kills"] + players[player["uuid"]]["kills"]
        else:
            player["team_number"] = None; player["uid"] = None # We null these properties as they are irrelevant and are different in every tournament.
            players[player["uuid"]] = player

    data_from_raw_request = [item[1] for item in sorted(players.items(), key=lambda x: x[1]["score"], reverse=True)[:15]]

    assert data_from_raw_request == data_from_wrapper