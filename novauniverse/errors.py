from devgoldyutils import Colours
from enum import Enum

class NovaError(Exception):
    """The base class of all NovaUniverse.py errors."""
    def __init__(self, message:str) -> None:
        """Raises this as a NovaUniverse.py exception."""
        super().__init__(Colours.RED.apply_to_string(message))