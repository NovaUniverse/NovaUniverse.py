from dataclasses import dataclass, field

from ....objects.nova_player import NovaBasicPlayer

@dataclass(repr=False)
class NovaOnlinePlayer(NovaBasicPlayer):
    """A online Nova Universe player. WOW their actually ONLINE! That's CRAZY!"""
    server_name:str = field(init=False)
    """Returns name of the server the player is in."""
    server_type_id:str = field(init=False)
    """Returns type id of the server the player is in."""
    server_type_name:str = field(init=False)
    """Returns type name of the server the player is in."""
    server_type_display_name:str = field(init=False)
    """Returns type display name of the server the player is in."""

    def __post_init__(self) -> None:
        super().__post_init__()

        self.server_name = self.get("server_name")
        self.server_type_id = self.get("server_type_id")
        self.server_type_name = self.get("server_type_name")
        self.server_type_display_name = self.get("server_type_display_name")