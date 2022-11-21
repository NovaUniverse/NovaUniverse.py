from __future__ import annotations
from enum import Enum
from typing import Type

from ..errors import NovaError, ErrorType

# SearchBy Enum class
# ---------------------
class SearchBy(Enum):
    id = 1
    name_ = 2

# Errors
# --------
class SearchGotNoArgs(NovaError):
    def __init__(self) -> None:
        super().__init__("Search() class must have either id or name passed. Like --> Search(name='UwU Bot')", ErrorType.ERROR)

class SearchNotCompletelySupported(NovaError):
    def __init__(self, searched_by, interface:object) -> None:
        super().__init__(f"Searching by '{searched_by}' not supported by '{interface.__class__.__name__}' interface/endpoint.", ErrorType.ERROR)

class HasNotBeenSearched(NovaError):
    def __init__(self) -> None:
        super().__init__("Can't return this property/method because you have not searched for this object.", ErrorType.ERROR)

# Search class
# ---------------
class Search():
    """Search by id or name if supported."""
    def __init__(self, id:str|int=None, name:str=None) -> None:
        self.__id = id
        self.__name = name

        self.__using_id = False
        self.__using_name = False

        if not self.__id == None: self.__using_id = True
        if not self.__name == None: self.__using_name = True
        
        if self.__using_id and self.__using_name:
            raise SearchGotNoArgs()

    def get_query(self) -> str|int|None:
        if self.search_by is SearchBy.id:
            return self.__id
        if self.search_by is SearchBy.name_:
            return self.__name
        return None

    @property
    def search_by(self) -> SearchBy|None:
        if self.__using_id:
            return SearchBy.id
        if self.__using_name:
            return SearchBy.name_

        return None

    def not_supported(self, interface: object):
        """Raises error to warn user this interface does not support searching by id/name."""
        raise SearchNotCompletelySupported(self.search_by.name, interface)