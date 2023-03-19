from ....objects.nova_dataclass import NovaDataclass

from dataclasses import dataclass, field

@dataclass(repr=False)
class MemberCount(NovaDataclass):
    data:dict = field(repr=False)

    total:int = field(init=False)
    bots:int = field(init=False)
    members:int = field(init=False)

    def __post_init__(self):
        self.total = self.get("total")
        self.bots = self.get("bots")

        self.members = ( self.total - self.bots )
        super().__post_init__()

@dataclass(repr=False)
class DiscordStats(NovaDataclass):
    data:dict = field(repr=False)

    member_count:MemberCount = field(init=False)
    
    def __post_init__(self):
        self.member_count = MemberCount(self.get("member_count"))
        super().__post_init__()