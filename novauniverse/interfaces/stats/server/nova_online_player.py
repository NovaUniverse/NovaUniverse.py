from dataclasses import dataclass, field

from ....objects.nova_player import NovaBasicPlayer

@dataclass
class NovaOnlinePlayer(NovaBasicPlayer):
    """A online Nova Universe player. WOW their actually ONLINE!"""

    server_name:str = field(init=False)
    """Returns name of the server the player is in."""
    server_type_id:str = field(init=False)
    """Returns type id of the server the player is in."""
    server_type_name:str = field(init=False)
    """Returns type name of the server the player is in."""
    server_type_display_name:str = field(init=False)
    """Returns type display name of the server the player is in."""

    def __init_subclass__(self, data:dict) -> None:
        self.server_name = data["server_name"]
        self.server_type_id = data["server_type_id"]
        self.server_type_name = data["server_type_name"]
        self.server_type_display_name = data["server_type_display_name"]