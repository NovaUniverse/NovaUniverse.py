from typing import List
from dataclasses import dataclass, field

from ....objects import NovaDataclass
from ....objects.nova_player import NovaBasicPlayer

@dataclass(repr=False)
class NovaServer(NovaDataclass):
    data:dict = field(repr=False)

    id:str = field(init=False)
    name:str = field(init=False)
    display_name:str = field(init=False)
    server_count:str = field(init=False)
    max_preview_players:int = field(init=False)
    available:bool = field(init=False)
    player_preview:List[NovaBasicPlayer] = field(init=False)
    
    def __post_init__(self):
        super().__post_init__()

        self.id = self.get("id")
        self.name = self.get("name")
        self.display_name = self.get("display_name")
        self.server_count = self.get("server_count")
        self.max_preview_players = self.get("max_preview_players")
        self.available = self.get("available")
        self.player_preview = [NovaBasicPlayer(player) for player in self.get("player_preview")]