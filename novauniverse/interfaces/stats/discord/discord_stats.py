from ....interfaces import InterfaceObject
from ....objects.nova_dataclass import NovaDataclass

from dataclasses import dataclass, field

@dataclass(repr=False)
class MemberCount(NovaDataclass):
    __data:dict = field(repr=False)

    total:int = field(init=False)
    bots:int = field(init=False)
    members:int = field(init=False)

    def __post_init__(self):
        self.total = self.__data["total"]
        self.bots = self.__data["bots"]

        self.members = ( self.total - self.bots )

@dataclass(repr=False)
class DiscordStats(NovaDataclass):
    __data:dict = field(repr=False)

    member_count:MemberCount = field(init=False)
    
    def __post_init__(self):
        self.set_data(self.__data)

        self.member_count = MemberCount(self.get("member_count"))