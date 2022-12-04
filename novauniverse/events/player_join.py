from . import Event, EventInfo
from ..interfaces.stats.server import Server, NovaOnlinePlayer

from ..api import NovaAPI
from ..api.endpoints import Endpoints

from typing import List

class PlayerJoin(Event):
    """Triggers each time a player joins any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__(self, EventInfo("player_join", NovaAPI(Endpoints.PLAYERS_ONLINE)))

        self.__old_players_list:List[NovaOnlinePlayer] = []
        self.__who_joined:NovaOnlinePlayer = None
        self.__first_run:bool = True

    def loop(self, data:dict) -> bool:
        data = [NovaOnlinePlayer(player_data) for player_data in data["players"]]

        # Lambda expression ignores players who are already on the server.
        players_difference:List[NovaOnlinePlayer] = (lambda players: players if self.__first_run is False else [])([player for player in data if player not in self.__old_players_list])

        if not players_difference == []:
            self.__who_joined = players_difference[0]
            self.__old_players_list = data
            return True
        else:
            self.__old_players_list = data
            self.__first_run = False
            return False

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_joined)