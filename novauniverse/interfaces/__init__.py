from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict
from devgoldyutils import LoggerAdapter

from .. import nova_logger, errors
from ..utils.search import Search, SearchBy

class Interface():
    """The base interface where all NovaUniverse.py endpoint interfaces inherit from."""
    def __init__(self) -> None:
        ...

class BasicInterface(Interface):
    """A basic interface, nothing more... nothing less..."""
    # TODO: Change this docstring lmao

    def __init__(self) -> None:
        super().__init__()


class SearchInterface(ABC, Interface):
    """Adds searching to a basic NU.PY interface. Use this to add searching functionality to your interfaces."""
    def __init__(self, supports: List[SearchBy], keys: Dict[SearchBy, str]) -> None:
        self.__supports = supports
        self.__keys = keys

        self.logger = LoggerAdapter(nova_logger, prefix="SearchInterface")
        super().__init__()

    @abstractmethod
    def search(self, query: Search | int | str, objects: List[object] = None) -> object | None:
        """It is recommended to use ``novauniverse.utils.search.Search()`` as a query but strings and integers will also work and be handled respectively."""

        if isinstance(query, str) or isinstance(query, int):
            if query.isnumeric():
                query = Search(id = query)
            else:
                query = Search(name = query)

        if query.search_by not in self.__supports:
            query.not_supported(self)

        self.logger.debug(f"Searching in '{self.__class__.__name__}' by '{query.search_by.name}' for '{query.get_query()}'...")
        # TODO: Add fuzzy search in the future.
        for object in objects:
            if object.__dict__[self.__keys[query.search_by]] == query.get_query():
                self.logger.info(f"Found {query.get_query()} by '{query.search_by.name}'.")
                return object

        return None


# Root Imports
# --------------
from ..api import NovaAPI, Endpoints