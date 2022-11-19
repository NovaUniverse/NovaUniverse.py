from .. import InterfaceObject

class NewsLetter(InterfaceObject):
    """A newsletter object but ."""
    def __init__(self, data:dict) -> None:
        self.__data:dict = data

        super().__init__(self, [
            ("title", self.title)
        ])

    @property
    def title(self) -> str:
        """Returns title of newsletter."""
        return self.__data["title"]

    @property
    def timestamp(self) -> str:
        """Returns timestamp as python datetime object."""