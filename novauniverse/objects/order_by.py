from enum import Enum
from ..errors import NovaError

class OrderBy(Enum):
    """Used in top player methods from tournament interfaces."""
    SCORE = 0
    KILLS = 1

class OrderByNotSupported(NovaError):
    def __init__(self, order_by:OrderBy) -> None:
        super().__init__(f"This method does not support ordering by '{order_by.name}'.")