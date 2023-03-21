"""
🐲 Nova Universe - A modern & maintained wrapper for the Nova Universe API written in Python.

Copyright (C) 2023 - Dev Goldy
"""

# Logging stuff
# ---------------
from .info import LOGGER_NAME
from devgoldyutils.logging import add_custom_handler, log

nova_logger = add_custom_handler(log.getLogger(LOGGER_NAME))
"""
The python ``logging.Logger()`` class for NovaUniverse.py.

---------------
### ``Example:``

You can disable and also adjust the level of logging from the api wrapper like this:

```python
import logging
nova_logger.setLevel(logging.DEBUG)
```

If your using the ``novauniverse.NovaClient`` class, a shortcut for enabling debugging would be this:

```python
NovaClient(debug=True)
```

If you want to completely disable logging like example warnings, you can do that with:

```python
nova_logger.setLevel(logging.NOTSET)
```
"""

nova_logger.setLevel(log.WARN)

# Configuration
# ---------------
from .configuration import Config
config = Config()
"""🐉 NovaUniverse.py config."""

# Endpoint Interfaces.
# ------------------------
#from .interfaces.news import News
from .interfaces.stats.discord import Discord
from .interfaces.stats.server import Server, NovaOnlinePlayer
from .interfaces.mcf import MCF
#from .interfaces.nova_games import NovaGames


#  Utils and Objects.
# ------------------------
#from .client import NovaClient
#from .events import Events

from .utils.search import Search

# Backend objects
from .objects.nova_player import NovaBasicPlayer
from .objects.timestamp import Timestamp
from .objects.tournaments import NovaBasicTournament, TournamentPlayer, TournamentTeam
from .objects.order_by import OrderBy

# Backend utils
from .api import Endpoints, NovaAPI, NovaCDN