import ast

from . import EndpointEvent
from ..interfaces.stats.server import NovaOnlinePlayer

from ..api.endpoints import Endpoints

from typing import Set

class PlayerLeave(EndpointEvent):
    """Triggers each time a player leaves any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__("player_leave", Endpoints.PLAYERS_ONLINE)

        self.__old_players:Set[str] = set()
        self.__who_left:NovaOnlinePlayer = None

    def loop(self, data:dict) -> bool:
        current_online_players = set([str(player_data) for player_data in data["players"]])

        for player in self.__old_players - current_online_players:
            self.__who_left = NovaOnlinePlayer(ast.literal_eval(player))
            self.__old_players = current_online_players
            return True
        
        self.__old_players = current_online_players
        return False

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_left)