"""
🐲 Nova Universe - A modern API wrapper for the minecraft server Nova Universe written in Python.

Copyright (C) 2022 - Dev Goldy
"""
import logging as log

from .logging import add_custom_handler
from .info import LOGGER_NAME

nova_logger = add_custom_handler(log.getLogger(LOGGER_NAME)); nova_logger.setLevel(log.WARN)
"""
The python ``logging.Logger()`` class for NovaUniverse.py.

--------------

You can adjust log level like this: 
```python
import logging
nova_logger.setLevel(log.DEBUG)
```
"""

# Endpoint Interfaces.
# ------------------------
from .interfaces.news import News
from .interfaces.stats.discord import Discord
from .interfaces.stats.server import Server, NovaOnlinePlayer


# Utils and Objects.
# ------------------------
from .client import NovaClient
from .events import Events

from .utils.search import Search