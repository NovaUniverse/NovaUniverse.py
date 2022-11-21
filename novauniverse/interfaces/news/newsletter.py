from __future__ import annotations

from .. import InterfaceObject

from ...utils.timestamp import Timestamp

from ... import nova_logger
from ...api.endpoints import BASE_DOMAIN
from .type import NewsLetterType
from .author import NewsLetterAuthor

class NewsLetter(InterfaceObject):
    """A newsletter object but ."""
    def __init__(self, data:dict) -> None:
        self.__data:dict = data

        super().__init__(id_and_name=(self.id, self.title), object_class=self,
            properties_to_represent = [
                ("id", self.id),
                ("title", self.title),
                ("timestamp", self.timestamp),
                ("author", self.author)
            ]
        )

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
    def time_ago(self) -> str|Timestamp:
        """
        Returns how long ago the newsletter was posted in a easily readable manner. Like this --> ``6 Months``. 
        If you want to customize this have a look at the ``NewsLetter().timestamp.date`` property.

        Returns ``NewsLetter().timestamp`` if not found.
        """
        try: # news/all does not return newsletter with 'time_ago' for some reason.
            return self.__data["time_ago"]
        except KeyError:
            nova_logger.warn("'time_ago' was not found so I'm gonna return timestamp instead.")
            return self.timestamp

    @property
    def full_url(self) -> str:
        """Returns the full url to this newsletter."""
        try: # news/all does not return newsletter with full url for some reason.
            return self.__data["full_url"]
        except KeyError:
            nova_logger.warn("'full_url' was not found so I'm generating the url with 'NewsLetter.id'.")
            return f"{BASE_DOMAIN}/newsletter/{self.id}"

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