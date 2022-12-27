from ....interfaces import InterfaceObject

from dataclasses import dataclass, field

@dataclass
class MemberCount:
    __data:dict = field(repr=False)

    total:int = field(init=False)
    bots:int = field(init=False)
    members:int = field(init=False)

    def __post_init__(self):
        self.total = self.__data["total"]
        self.bots = self.__data["bots"]

        self.members = ( self.total - self.bots )

class DiscordStats(InterfaceObject):
    def __init__(self, data:dict):
        self.__data = data

        super().__init__(id_and_name=(None, None), object_class=self, 
            properties_to_represent=[
                ("member_count", self.member_count)
            ]
        )

    @property
    def member_count(self) -> MemberCount:
        return MemberCount(self.__data["member_count"])