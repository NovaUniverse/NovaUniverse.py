from __future__ import annotations

import abc
from dataclasses import dataclass
from enum import Enum

from .. import nova_logger

@dataclass
class EventInfo:
    """Details about a event."""
    code_name:str


# Base Event Class
# -------------------------
class Event():
    """A base class for all NovaUniverse.py events."""
    def __init__(self, event_class:object, info:EventInfo):
        __metaclass__ = abc.ABCMeta

        self.__event_class = event_class
        self.__info = info

        self.__functions_to_trigger:list = []

    def code_name(self) -> str:
        """Returns code name of event."""
        return self.__info.code_name


    @abc.abstractmethod
    def loop(self) -> bool:
        """
        This method is called each ``NovaClient`` 💖heartbeat if the event is in use.

        -------------------
        
        Returning ``True`` indicates to ``NovaClient`` that the data has changed and it can trigger the event.

        Returning ``False`` indicates to ``NovaClient`` that the data has not changed and it shouldn't trigger the event.
        """
        ...

    @abc.abstractmethod
    def trigger_event(self):
        """This method is ran when ``NovaClient`` gets an indication that the data has changed."""
        ...


    def add_function(self, func):
        """Used by ``NovaClient`` to add functions to events."""
        self.__functions_to_trigger.append(func)


# Import all events under this module.
# --------------------------------------------
from . import *

class Events(Enum):
    """An enum class of all available events. These can be used in ``NovaClient().on_event()`` function decorator."""
    PLAYER_JOIN = 1