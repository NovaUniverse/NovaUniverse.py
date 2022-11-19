from .. import InterfaceObject

from ...utils.timestamp import Timestamp

class NewsLetter(InterfaceObject):
    """A newsletter object but ."""
    def __init__(self, data:dict) -> None:
        self.__data:dict = data

        super().__init__(self, [
            ("title", self.title),
            ("timestamp", self.timestamp)
        ])

    @property
    def title(self) -> str:
        """Returns title of newsletter."""
        return self.__data["title"]

    @property
    def timestamp(self) -> Timestamp:
        """Returns timestamp as python datetime object."""
        return Timestamp(self.__data["timestamp"])

    @property
    def html(self) -> str:
        """Returns the html of this letter as a string."""
        return self.__data["html"]

    