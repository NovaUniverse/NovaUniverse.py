from __future__ import annotations

from ....utils.search import Search, SearchBy
from ... import Interface, InterfaceObject

from typing import List, Any

from .server_info import ServerInfo
from .nova_online_player import NovaOnlinePlayer

class Server(Interface):
    """
    The interface for NovaAPI's ``/stats/extended`` endpoint.
    Allows you to get all 🌐server stats/info and see which players are 🟢online.
    """
    def __init__(self):
        super().__init__()
        
        self.stats_extended_api = self.api(self.endpoints.STATS_EXTENDED)
        self.players_online_api = self.api(self.endpoints.PLAYERS_ONLINE)

    def get_stats(self) -> ServerInfo:
        """Get's and returns all server stats."""
        return ServerInfo(self.stats_extended_api.get(), self.players_online_api.get())
    
    def get_online_players(self) -> List[NovaOnlinePlayer]:
        """Returns list of just the online players."""
        return [NovaOnlinePlayer(player_data) for player_data in self.players_online_api.get()["players"]]