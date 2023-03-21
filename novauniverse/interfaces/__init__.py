
from abc import ABC, abstractmethod
from typing import List
from devgoldyutils import LoggerAdapter

from .. import nova_logger
from ..api import NovaAPI, Endpoints
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


# TODO: Finish this off..
class SearchInterface(ABC, Interface):
    """Adds searching to a basic NU.PY interface. Use this to add searching functionality to your interfaces."""
    def __init__(self, supports:List[SearchBy]) -> None:
        self.__supports = supports

        self.logger = LoggerAdapter(nova_logger, prefix="SearchInterface")
        super().__init__()

    @abstractmethod
    def find(self, search:Search, object_list=None) -> InterfaceObject|None:
        if isinstance(search, Search):
            if not search.search_by in self.__supports:
                search.not_supported(self.__interface_class)
            
            # Search by id
            # --------------
            if search.search_by is SearchBy.id:
                self.logger.debug(f"Searching for '{self.__interface_class.__name__}' by id...")

                for object in object_list:
                    if object.id == search.get_query():
                        self.logger.info(f"Found '{self.__interface_class.__name__}' by id.")
                        return object

            # Search by name
            # --------------
            if search.search_by is SearchBy.name_:
                self.logger.debug(f"Searching for '{self.__interface_class.__name__}' by name...")

                for object in object_list:
                    if object.name == search.get_query():
                        self.logger.info(f"Found '{self.__interface_class.__name__}' by name.")
                        return object
        
        else:
            raise NovaError(f"You must use the 'novauniverse.Search()' class for searching in '{self.__interface_class.__name__}'.")

        return None