from dataclasses import dataclass, field

from ....objects import Timestamp, NovaDataclass

@dataclass
class System(NovaDataclass):
    data:dict = field(repr=False)

    localtime:Timestamp = field(init=False)

    def __post_init__(self):
        super().__post_init__()

        self.localtime = Timestamp(self.get("localtime"))