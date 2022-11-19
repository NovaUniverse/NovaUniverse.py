from devgoldyutils import Console
from enum import Enum

class ErrorType(Enum):
    """A enum class of error types. These error types can be passed to the NovaError exception class."""
    ERROR = 1
    # Room here for more...

class NovaError(Exception):
    """The base class of all NovaUniverse.py errors."""
    def __init__(self, message:str, type:ErrorType=1) -> None:
        """Raises this as a NovaUniverse.py exception."""
        
        super().__init__(Console().RED(message))