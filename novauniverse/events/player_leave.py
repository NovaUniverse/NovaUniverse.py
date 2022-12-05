import ast

from . import Event, EventInfo
from ..interfaces.stats.server import NovaOnlinePlayer

from ..api_ import NovaAPI
from ..api_.endpoints import Endpoints

from typing import Set

class PlayerLeave(Event):
    """Triggers each time a player leaves any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__(self, EventInfo("player_leave", NovaAPI(Endpoints.PLAYERS_ONLINE)))

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

        """
        if not players_difference == []:
            player_who_left_uuid = players_difference[0].uuid
            
            for player in self.__old_players_list:
                if player.uuid == player_who_left_uuid:
                    self.__who_left = player
                
            self.__old_players_list = data
            return True
        else:
            self.__old_players_list = data
            return False
        """

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_left)