import ast

from . import Event, EventInfo
from ..interfaces.stats.server import NovaOnlinePlayer

from ..api import NovaAPI
from ..api.endpoints import Endpoints

from typing import Set

class PlayerJoin(Event):
    """Triggers each time a player joins any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__(self, EventInfo("player_join", NovaAPI(Endpoints.PLAYERS_ONLINE)))

        self.__old_players:Set[str] = set()
        self.__who_joined:NovaOnlinePlayer = None
        self.__first_run:bool = True

    def loop(self, data:dict) -> bool:
        current_online_players = set([str(player_data) for player_data in data["players"]])

        for player in current_online_players - self.__old_players:
            if not self.__first_run:
                self.__who_joined = NovaOnlinePlayer(ast.literal_eval(player))
                self.__old_players = current_online_players
                return True

        self.__first_run = False
        self.__old_players = current_online_players
        return False

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_joined)