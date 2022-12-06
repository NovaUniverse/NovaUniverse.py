from dataclasses import dataclass, field

@dataclass
class NovaBasicPlayer:
    """A very basic nova universe player class."""
    __data:dict = field(repr=False)

    uuid:str = field(init=False)
    """Returns UUID of novauniverse player."""
    username:str = field(init=False)
    """Returns username of novauniverse player."""

    def __post_init__(self):
        self.uuid = self.__data["uuid"]
        self.username = self.__data["username"]

        try:
            self.__post_init_subclass__(self.__data)
        except TypeError:
            pass