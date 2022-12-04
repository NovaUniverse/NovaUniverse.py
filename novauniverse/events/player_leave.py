from . import Event, EventInfo
from ..interfaces.stats.server import Server, NovaOnlinePlayer

from ..api import NovaAPI
from ..api.endpoints import Endpoints

from typing import List

class PlayerLeave(Event):
    """Triggers each time a player leaves any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__(self, EventInfo("player_leave", NovaAPI(Endpoints.PLAYERS_ONLINE)))

        self.__old_players_list:List[NovaOnlinePlayer] = []
        self.__who_left:NovaOnlinePlayer = None

    def loop(self, data:dict) -> bool:
        data = [NovaOnlinePlayer(player_data) for player_data in data["players"]]
        
        players_difference = [player for player in self.__old_players_list if player not in data]

        if not players_difference == []:
            self.__who_left = players_difference[0]
            self.__old_players_list = data
            return True
        else:
            self.__old_players_list = data
            return False

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_left)