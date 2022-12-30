from . import *
from .nova_dataclass import NovaDataclass

# Very Internal stuff
# ---------------------

def _inheritance_support(self, data:dict):
    """Adds inheritance support to dataclasses. This should only be used internally in NovaUniverse.py!"""
    try:
        self.__post_init_subclass__(data)
    except (TypeError, AttributeError) as e:
        pass