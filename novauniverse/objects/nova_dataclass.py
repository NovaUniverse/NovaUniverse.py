from dataclasses import dataclass, field

from prettyprinter import cpprint, install_extras
install_extras(include=["dataclasses"])

from io import StringIO

from .. import config

class NovaDataclass:
    """The root NovaUniverse.py class that all dataclasses inherited from."""

    # BETTER dataclass representation, also it's coloured. 🌈
    # ---------------------------------------------------------
    def __repr__(self) -> str:
        if config.performance_mode: # I've heard pretty-printer can be a bit slow, so to save time I've disabled it in performance mode.
            return super().__repr__()
        
        text_stream = StringIO()
        cpprint(self, stream=text_stream, depth=3, max_seq_len=1)
        text_stream.seek(0)
        return text_stream.read()