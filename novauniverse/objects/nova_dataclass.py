from __future__ import annotations
from io import StringIO
from dataclasses import dataclass, field
from typing import Any

from prettyprinter import cpprint, install_extras
install_extras(include=["dataclasses"])

from .. import config, nova_logger

@dataclass
class NovaDataclass:
    """The root NovaUniverse.py class that all dataclasses inherited from."""
    __dict_data:dict = field(init=False, repr=False, default=None)

    # BETTER dataclass representation, also it's coloured. 🌈
    # ---------------------------------------------------------
    def __repr__(self) -> str:
        if config.performance_mode: # I've heard pretty-printer can be a bit slow, so to save performance I've disabled it in performance mode.
            return super().__repr__()
        
        text_stream = StringIO()
        cpprint(self, stream=text_stream, depth=3, max_seq_len=1)
        text_stream.seek(0)
        return text_stream.read()

    def set_data(self, data:dict):
        self.__dict_data = data

    def get(self, key:Any, data:dict=None, default:Any=None) -> Any|dict|None:
        """Get's and returns value of key in data dictionary."""
        try:
            if data is None: data = self.__dict_data
            return data[key]
        except KeyError:
            if not data in [{}, None]:
                nova_logger.warn(
                    f"The key '{key}' was not found in the dictionary so '{default}' was returned. It looks like something changed in the API recently. PLEASE update the library if you haven't already."
                )
            return default
