from datetime import datetime
from dataclasses import dataclass, field

from . import NovaDataclass

@dataclass(repr=False)
class Timestamp(NovaDataclass):
    """A NovaUniverse API timestamp object."""
    data:dict = field(repr=False)

    date:datetime = field(init=False)
    """The date and time at Zeeraa's house right now. Wait what, why do you want to stalk his date and time."""
    timezone:str = field(init=False)
    timezone_type:int = field(init=False)

    def __post_init__(self):
        """Returns timestamp as python datetime object and more."""
        super().__post_init__()

        self.date = datetime.strptime(self.get("date"), "%Y-%m-%d %H:%M:%S.%f")
        self.timezone = self.get("timezone")
        self.timezone_type = self.get("timezone_type")