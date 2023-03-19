from dataclasses import dataclass, field
from . import NovaDataclass

@dataclass(repr=False)
class NovaBasicPlayer(NovaDataclass):
    """A very basic nova universe player class."""
    data:dict = field(repr=False)

    uuid:str = field(init=False)
    """Returns UUID of novauniverse player."""
    username:str = field(init=False)
    """Returns username of novauniverse player."""
    name:str = field(init=False)
    """Aliases of ``username``."""

    def __post_init__(self):
        super().__post_init__()

        self.uuid = self.get("uuid")
        self.username = self.get("username")

        self.name = self.username