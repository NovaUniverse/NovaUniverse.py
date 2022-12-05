from __future__ import annotations

import abc
from typing import Type, List, Tuple, Any

from .. import nova_logger
from ..errors import NovaError, ErrorType
from ..api import NovaAPI, Endpoints
from ..utils.search import Search, SearchBy

# Base Interface & Object Class
# -------------------------
class Interface():
    """A base class for all NovaUniverse API endpoints."""
    def __init__(self):
        self.api:Type[NovaAPI] = NovaAPI
        self.endpoints:Type[Endpoints] = Endpoints
        
class InterfaceObject():
    """Base class for objects in all NovaUniverse.py interfaces."""
    def __init__(self, id_and_name:Tuple[int, str], object_class:object, properties_to_represent:List[Tuple[str, Any]]=[]):
        self.__id = id_and_name[0]
        self.__name = id_and_name[1]
        self.__object_class = object_class

        self.__string_repr = ""
        for property in properties_to_represent:
            self.__string_repr += f"\u001b[38;5;51m{property[0]}\u001b[0m='{property[1]}', "

    @property
    def id(self) -> int|None:
        """Tries to return the id."""
        return self.__id

    @property
    def name(self) -> str|None:
        """Tries to return the name."""
        return self.__name

    def __repr__(self) -> str:
        try:
            return (
                f'\u001b[32m{self.__object_class.__class__.__name__}\u001b[0m' + 
                f'({self.__string_repr[:-2]})'
            )
        except AttributeError:
            return super().__repr__()

class SearchInterface(Interface):
    """Adds searching to the basic interface class. Use this to add searching functionality to interfaces."""
    def __init__(self, interface_class:object, supports:List[SearchBy]):
        __metaclass__ = abc.ABCMeta
        super().__init__()

        self.__interface_class = interface_class.__class__
        self.__supports = supports

    @abc.abstractmethod
    def find(self, search_class:Search, object_list:List[InterfaceObject]=None) -> InterfaceObject|None:
        if isinstance(search_class, Search):
            if not search_class.search_by in self.__supports:
                search_class.not_supported(self.__interface_class)
            
            # Search by id
            # --------------
            if search_class.search_by is SearchBy.id:
                nova_logger.debug(f"Searching for '{self.__interface_class.__name__}' by id...")

                for object in object_list:
                    if object.id == search_class.get_query():
                        nova_logger.info(f"Found '{self.__interface_class.__name__}' by id.")
                        return object

            # Search by name
            # --------------
            if search_class.search_by is SearchBy.name_:
                nova_logger.debug(f"Searching for '{self.__interface_class.__name__}' by name...")

                for object in object_list:
                    if object.name == search_class.get_query():
                        nova_logger.info(f"Found '{self.__interface_class.__name__}' by name.")
                        return object
        
        else:
            raise NovaError(f"You must use the 'novauniverse.Search()' class for searching in '{self.__interface_class.__name__}'.", ErrorType.ERROR)

        return None
        


# Import all interfaces under this module.
# --------------------------------------------
from . import *