from typing import Type
from ..api import NovaAPI, Endpoints

from typing import List, Tuple

# Base Interface & Object Class
# -------------------------
class Interface():
    """Base class for all NovaUniverse.py interfaces."""
    def __init__(self):
        self.api:Type[NovaAPI] = NovaAPI
        self.endpoints:Type[Endpoints] = Endpoints
        
class InterfaceObject():
    """Base class for objects in all NovaUniverse.py interfaces."""
    def __init__(self, object_class:object, properties_to_represent:List[Tuple[str, object]]=[]):
        self.__object_class = object_class

        self.__string_repr = ""
        for property in properties_to_represent:
            self.__string_repr += f"{property[0]}='{property[1]}', "

    def __repr__(self) -> str:
        return (
            f'{self.__object_class.__class__.__name__}' + 
            f'({self.__string_repr[:-2]})'
        )

# Import all interfaces under this module.
# --------------------------------------------
from . import *