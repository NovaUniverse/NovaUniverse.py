"""
🐲 Nova Universe - A modern API wrapper for the minecraft server Nova Universe written in Python.

Copyright (C) 2022 - Dev Goldy

----------------------------
.. include:: ../README.md

<br>
"""

import logging as log

from .logging import add_custom_handler
from .info import LOGGER_NAME

nova_logger = add_custom_handler(log.getLogger(LOGGER_NAME))
"""
The python ``logging.Logger()`` class for NovaUniverse.py.

---------------
### ***``Example:``***

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

# Endpoint Interfaces.
# ------------------------
from .interfaces.news import News
from .interfaces.stats.discord import Discord
from .interfaces.stats.server import Server, NovaOnlinePlayer
from .interfaces.mcf import MCF


# Utils and Objects.
# ------------------------
from .client import NovaClient
from .events import Events

from .utils.search import Search
