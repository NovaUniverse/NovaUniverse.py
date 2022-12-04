from . import Event, EventInfo
from ..interfaces.stats.server import Server, nova_online_player

class PlayerJoin(Event):
    """Triggers each time a player joins any lobby on the Nova Universe network."""
    def __init__(self):
        super().__init__(self, EventInfo("player_join"))

        self.__old_players_list:nova_online_player.NovaOnlinePlayer = []
        self.__who_joined:nova_online_player.NovaOnlinePlayer = None

    def loop(self) -> bool:
        data = Server().get_online_players()
        players_difference = [player for player in data if player not in self.__old_players_list]

        if not players_difference == []:
            self.__who_joined = players_difference[0]
            self.__old_players_list = data
            return True
        else:
            self.__old_players_list = data
            return False

    def trigger_event(self):
        for function in self.functions_to_trigger:
            function(self.__who_joined)