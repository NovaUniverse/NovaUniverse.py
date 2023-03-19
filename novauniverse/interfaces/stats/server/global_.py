from dataclasses import dataclass, field

from ....objects import NovaDataclass

@dataclass(repr=False)
class Global(NovaDataclass):
    data:dict = field(repr=False)

    player_count:int = field(init=False)
    """Returns global player count of Nova Universe."""
    server_count:int = field(init=False)
    """Returns global server count of Nova Universe."""
    
    def __post_init__(self):
        super().__post_init__()

        self.player_count = self.get("player_count")
        self.server_count = self.get("server_count")