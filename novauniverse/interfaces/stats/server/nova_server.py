from typing import List
from dataclasses import dataclass, field

from ....objects.nova_player import NovaBasicPlayer

@dataclass
class NovaServer:
    __data:dict = field(repr=False)

    id:str = field(init=False)
    name:str = field(init=False)
    display_name:str = field(init=False)
    server_count:str = field(init=False)
    max_preview_players:int = field(init=False)
    available:bool = field(init=False)
    player_preview:List[NovaBasicPlayer] = field(init=False)
    
    def __post_init__(self):
        self.id = self.__data["id"]
        self.name = self.__data["name"]
        self.display_name = self.__data["display_name"]
        self.server_count = self.__data["server_count"]
        self.max_preview_players = self.__data["max_preview_players"]
        self.available = self.__data["available"]
        self.player_preview = [NovaBasicPlayer(player) for player in self.__data["player_preview"]]