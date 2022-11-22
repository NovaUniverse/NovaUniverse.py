from dataclasses import dataclass, field

from ....objects.timestamp import Timestamp

@dataclass
class System:
    __data:dict = field(repr=False)

    localtime:Timestamp = field(init=False)

    def __post_init__(self):
        self.localtime = Timestamp(self.__data["localtime"])