from __future__ import annotations

from .. import Interface
from .newsletter import NewsLetter

from typing import List

class News(Interface):
    def __init__(self):
        """Class to inference with NovaUniverse API news endpoint."""
        super().__init__()
        
        self.news_all_api = self.api(self.endpoints.NEWS_ALL)
        self.news_latest_api = self.api(self.endpoints.NEWS_LATEST)

    def get_all(self) -> List[NewsLetter]:
        """Returns all newsletters from api in a list. Returns empty list if none."""
        newsletters:List[NewsLetter] = []

        data = self.news_all_api.get()["data"]

        for entry in data["entries"]:
            newsletters.append(NewsLetter(entry))

        return newsletters

    def get_latest(self) -> List[NewsLetter]|None:
        """Returns the latest newsletter from api. Returns None if not found."""
        data = self.news_latest_api.get()["data"]

        if data["found"]:
            return NewsLetter(self.news_latest_api.get()["data"]["latest"])
        else:
            return None