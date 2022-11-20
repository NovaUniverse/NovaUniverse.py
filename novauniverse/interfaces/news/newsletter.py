from .. import InterfaceObject

from ...utils.timestamp import Timestamp

from .type import NewsLetterType
from .author import NewsLetterAuthor

class NewsLetter(InterfaceObject):
    """A newsletter object but ."""
    def __init__(self, data:dict) -> None:
        self.__data:dict = data

        super().__init__(self, [
            ("id", self.id),
            ("title", self.title),
            ("timestamp", self.timestamp),
            ("author", self.author)
        ])

    @property
    def id(self) -> int:
        """Returns the id of the newsletter."""
        return self.__data["id"]

    @property
    def title(self) -> str:
        """Returns title of newsletter."""
        return self.__data["title"]

    @property
    def timestamp(self) -> Timestamp:
        """Returns timestamp as python datetime object."""
        return Timestamp(self.__data["timestamp"])

    @property
    def time_ago(self) -> str:
        """
        Returns how long ago the newsletter was posted in a easily readable manner. Like this --> ``6 Months``. 
        If you want to customize this have a look at the ``NewsLetter().timestamp.date`` property.
        """
        return self.__data["time_ago"]

    @property
    def full_url(self) -> str:
        """Returns the full url to this newsletter."""
        return self.__data["full_url"]

    @property
    def type(self) -> NewsLetterType:
        """Returns the newsletter type. UwU"""
        return NewsLetterType(self.__data["type"])

    @property
    def author(self) -> NewsLetterAuthor:
        """Returns the author of the newsletter."""
        return NewsLetterAuthor(self.__data["author"])

    @property
    def html(self) -> str:
        """Returns the html of this letter as a string."""
        return self.__data["html"]

    @property
    def raw(self) -> str:
        """Returns the raw bbcode as a string."""
        return self.__data["raw"]