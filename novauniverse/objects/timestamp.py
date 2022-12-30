from datetime import datetime
from dataclasses import dataclass, field

from . import _inheritance_support

@dataclass
class Timestamp:
    """A NovaUniverse API timestamp object."""
    __data:dict = field(repr=False)

    date:datetime = field(init=False)
    """The date and time at Zeeraa's house right now. Wait what, why do you want to stalk his date and time."""
    timezone:str = field(init=False)
    timezone_type:int = field(init=False)

    def __post_init__(self):
        """Returns timestamp as python datetime object and more."""
        self.date = datetime.strptime(self.__data["date"], "%Y-%m-%d %H:%M:%S.%f")
        self.timezone = self.__data["timezone"]
        self.timezone_type = self.__data["timezone_type"]

        _inheritance_support(self, self.__data)