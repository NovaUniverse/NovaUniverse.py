from dataclasses import dataclass, field

@dataclass
class Global:
    __data:dict = field(repr=False)

    player_count:int = field(init=False)
    """Returns global player count of Nova Universe."""
    server_count:int = field(init=False)
    """Returns global server count of Nova Universe."""
    

    def __post_init__(self):
        self.player_count = self.__data["player_count"]
        self.server_count = self.__data["server_count"]