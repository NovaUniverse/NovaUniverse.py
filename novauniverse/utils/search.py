from __future__ import annotations
from typing import overload, NoReturn
from enum import Enum

from ..errors import NovaError

# SearchBy Enum class
# ---------------------
class SearchBy(Enum):
    ID = 1
    NAME = 2

# Errors
# --------
class SearchGotNoArgs(NovaError):
    def __init__(self) -> None:
        super().__init__("'Search()' class must have either id or name passed. Like --> Search(name='UwU Dev Goldy')")

class SearchNotCompletelySupported(NovaError):
    def __init__(self, searched_by, interface:object) -> None:
        super().__init__(f"Searching by '{searched_by}' not supported by '{interface.__class__.__name__}' interface/endpoint.")

# Search class
# ---------------
class Search():
    """A util that allows you to search within an interface by id or name if supported."""
    @overload
    def __init__(self, id:str|int) -> None:
        """Search by id."""
        ...
    
    @overload
    def __init__(self, name:str) -> None:
        """Search by name."""
        ...

    def __init__(self, id:str|int=None, name:str=None) -> None:
        self.id = id
        self.name = name

        self.search_by:SearchBy|None = None

        if self.name is not None:
            self.search_by = SearchBy.NAME
        if self.id is not None:
            self.search_by = SearchBy.ID
        
        if self.search_by is None:
            raise SearchGotNoArgs()

    def get_query(self) -> str|int|None:
        """Returns the query."""
        if self.search_by is SearchBy.ID:
            return self.id
        if self.search_by is SearchBy.NAME:
            return self.name
        return None

    def not_supported(self, interface: object) -> NoReturn:
        """Raises error to warn user this interface does not support searching by id/name."""
        raise SearchNotCompletelySupported(self.search_by.name, interface)