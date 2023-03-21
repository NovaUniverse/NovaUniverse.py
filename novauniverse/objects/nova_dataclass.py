from __future__ import annotations
from io import StringIO
from dataclasses import dataclass
from devgoldyutils import DictDataclass

from prettyprinter import cpprint, install_extras
install_extras(include=["dataclasses"])

from .. import config, nova_logger

@dataclass
class NovaDataclass(DictDataclass):
    """The root NovaUniverse.py class that all dataclasses inherited from."""
    def __post_init__(self):
        self.logger = nova_logger
        super().__post_init__()

    # BETTER dataclass representation, also it's coloured. 🌈
    # ---------------------------------------------------------
    def __repr__(self) -> str:
        if config.performance_mode: # I've heard pretty-printer can be a bit slow, so to save performance I've disabled it in performance mode.
            return super().__repr__()
        
        text_stream = StringIO()
        cpprint(self, stream=text_stream, depth=3, max_seq_len=1)
        text_stream.seek(0)
        return text_stream.read()