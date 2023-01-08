from dataclasses import dataclass, field
from . import _inheritance_support, NovaDataclass


@dataclass(repr=False)
class NovaBasicPlayer(NovaDataclass):
    """A very basic nova universe player class."""
    __data:dict = field(repr=False)

    uuid:str = field(init=False)
    """Returns UUID of novauniverse player."""
    username:str = field(init=False)
    """Returns username of novauniverse player."""
    name:str = field(init=False)
    """Aliases of ``username``."""

    def __post_init__(self):
        self.set_data(self.__data)
        
        self.uuid = self.get("uuid")
        self.username = self.get("username")

        self.name = self.username

        _inheritance_support(self, self.__data)