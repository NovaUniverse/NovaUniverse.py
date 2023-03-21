import logging as log
from devgoldyutils import DevGoldyUtilsError

from . import nova_logger

class NovaError(DevGoldyUtilsError):
    """The base class of all NovaUniverse.py errors."""
    def __init__(self, message: str, logger: log.Logger = None):
        """Raises a NovaUniverse.py exception."""
        if logger is None:
            logger = nova_logger

        super().__init__(message, logger)