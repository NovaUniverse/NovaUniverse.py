from ....objects import NovaDataclass
from dataclasses import dataclass, field

from .global_ import Global
from .player_preview import PlayerPreview
from .nova_server import NovaServer
from .system import System
from .nova_online_player import NovaOnlinePlayer

from typing import List

@dataclass
class ServerInfo(NovaDataclass):
    data:dict = field(repr=False)
    players_data:dict = field(repr=False)

    global_:Global = field(init=False)
    """Returns class that contains global ``player_count`` and ``server_count``."""
    player_count:int = field(init=False)
    """Returns global player count of Nova Universe."""
    server_count:int = field(init=False)
    """Returns global server count of Nova Universe."""
    player_preview:PlayerPreview = field(init=False)
    """Returns player preview."""
    servers:List[NovaServer] = field(init=False)
    """Returns all servers on the Nova Universe network."""
    online_players:List[NovaOnlinePlayer] = field(init=False)
    """Returns all players that are online as NovaBasicPlayer object."""
    cached:bool = field(init=False)
    """Returns whether this data is cached or not."""
    system:System = field(init=False)
    """Returns the system class that lets you see get details like the localtime."""

    def __post_init__(self):
        super().__post_init__()

        self.global_ = Global(self.get("global"))
        self.player_count = self.global_.player_count
        self.server_count = self.global_.server_count
        self.player_preview = PlayerPreview(self.get("player_preview"))
        self.servers = [NovaServer(server_data) for server_data in self.get("servers")]
        self.online_players = [NovaOnlinePlayer(player_data) for player_data in self.get("players", data=self.players_data, default_value=[])]
        self.cached = self.get("cached")
        self.system = System(self.get("system"))