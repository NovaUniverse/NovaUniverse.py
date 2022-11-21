from __future__ import annotations

from ...utils.search import Search, SearchBy
from .. import Interface, SearchInterface, InterfaceObject
from .newsletter import NewsLetter

from typing import List, Any

class News(SearchInterface):
    """
    The interface for NovaAPI's ``/news`` endpoint.
    Allows you to get latest, get all and search for 📰newsletters.
    """
    def __init__(self):
        super().__init__(self, supports=[SearchBy.id, SearchBy.name_])
        
        self.__news_all_api = self.api(self.endpoints.NEWS_ALL)
        self.__news_latest_api = self.api(self.endpoints.NEWS_LATEST)

    def find(self, search: Search) -> NewsLetter | None:
        """Find/Search for 📰newsletters."""
        return super().find(search, self.get_all())

    def get_all(self) -> List[NewsLetter]:
        """Returns all 📰newsletters from api in a list. Returns empty list if none."""
        newsletters:List[NewsLetter] = []

        data = self.__news_all_api.get()["data"]

        for entry in data["entries"]:
            newsletters.append(NewsLetter(entry))

        return newsletters

    def get_latest(self) -> NewsLetter|None:
        """Returns the latest 📰newsletter from api. Returns None if not found."""
        data = self.__news_latest_api.get()["data"]

        if data["found"]:
            return NewsLetter(data["latest"])
        else:
            return None