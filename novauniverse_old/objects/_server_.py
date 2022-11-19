from datetime import datetime
from typing import List
from .. import API

class BasicServer(object):
    """Class for basic server stats."""
    def __init__(self, ENDPOINT:str, ENDPOINT_2:str, cached:bool, players_online:dict):
        self.ENDPOINT = ENDPOINT
        self.ENDPOINT_2 = ENDPOINT_2

        self._cached = cached

        self.players_online_ = players_online

    from . import _player_

    class online_player(_player_.basic_player):
        def __init__(self, ENDPOINT: str, uuid: str, username: str, server_name:str, server_type_id:str, server_type_name:str, server_type_display_name:str):
            id = None # I don't have an easy and quick way to grab the player's id, due to it not being in this section of the api.
            super().__init__(id, uuid, username)

            self.server_name_ = server_name
            self.server_type_id_ = server_type_id
            self.server_type_name_ = server_type_name
            self.server_type_display_name_ = server_type_display_name

    @property
    def player_count(self) -> int:
        """The amount of players on the network right now. (LIVE)"""
        return int(API.update(self, "player_count"))

    @property
    def server_count(self) -> int:
        """The amount of servers online on the network right now. (LIVE)"""
        return int(API.update(self, "server_count"))

    @property
    def cached(self) -> bool:
        """Has this data been cached by the API or not."""
        if self._cached == "true": return True
        else: return False

    @property
    def localtime(self) -> datetime:
        """The local time at Zeeraa's house... uMm, returns as python datetime object. (LIVE)"""
        return datetime.strptime(API.update(self, "localtime")["date"], '%Y-%m-%d %H:%M:%S.%f')

    @property
    def timezone(self) -> str:
        """The name of the timezone the API server is in."""
        return str(API.update(self, "localtime")["timezone"])

    @property
    def players(self) -> List[online_player]:
        """Returns list of players online as player object."""
        players_list = []
        for player_ in self.players_online_:
            players_list.append(self.online_player(self.ENDPOINT_2, player_["uuid"], player_["username"], player_["server_name"], 
            player_["server_type_id"], player_["server_type_name"], player_["server_type_display_name"]))

        return players_list

    players_online = players
    online_players = players
    
    datetime = localtime
    time = localtime

class Server(object):
    """Class for extended server stats."""
    def __init__(self, ENDPOINT:str, cached:bool):
        super().__init__(ENDPOINT, cached)