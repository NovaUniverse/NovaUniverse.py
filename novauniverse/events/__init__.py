from __future__ import annotations

import abc
from typing import Type, List, Tuple, Any

from .. import nova_logger
from ..errors import NovaError, ErrorType
from ..api import NovaAPI, Endpoints
from ..utils.search import Search, SearchBy

# Base Event Class
# -------------------------
class Event():
    """A base class for all NovaUniverse.py events."""
    def __init__(self):
        self.api:Type[NovaAPI] = NovaAPI
        self.endpoints:Type[Endpoints] = Endpoints


# Import all interfaces under this module.
# --------------------------------------------
from . import *