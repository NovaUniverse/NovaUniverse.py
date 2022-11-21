"""
🐲 Nova Universe - A modern API wrapper for the minecraft server Nova Universe written in Python.

Copyright (C) 2022 - Dev Goldy
"""
import logging as log
from .logging import add_custom_handler

from .info import LOGGER_NAME

nova_logger = add_custom_handler(log.getLogger(LOGGER_NAME))

# Endpoint Interfaces.
# ------------------------
from .interfaces.news import News


# Utils and Objects.
# ------------------------
from .utils.search import Search