[![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)](https://discord.gg/4gZSVJ7)
[![PyPI version](https://badge.fury.io/py/novauniverse.svg)](https://pypi.org/project/novauniverse/)
[![Python Badge](https://img.shields.io/pypi/pyversions/novauniverse?style=flat)](https://pypi.org/project/novauniverse/ "Supported python versions.")
[![Docs Badge](https://img.shields.io/static/v1?label=docs&message=Available&color=light-green)](https://nupy.devgoldy.me/)

<p align="center">
 <img src="https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png" width="500" />
</p>

### 🐍[``novauniverse.py``](https://pypi.org/project/novauniverse/) - A modern & maintained wrapper for the [Nova Universe API](https://novauniverse.net/api/) written in Python.

#### ℹ Notice: 2.0 is currently in development so not all api endpoints are implemented.

<p align="right">
 <img align="left" src="https://raw.githubusercontent.com/NovaUniverse/NovaUniverse.py/v2/assets/logo.png" width="180" />
 
 <h2>What is Nova Universe.py?</h2>
 NovaUniverse.py is a API wrapper for the minecraft server <a href="https://novauniverse.net/">Nova Universe</a> that allows you to access the Nova Universe <a href="https://novauniverse.net/api">API</a> in a fast object oriented way in Python. One of the bonuses is that it was developed by one of the devs at NovaUniverse.
</p>

<br>

## *Install/Set Up*
1. ~~**Install package from pypi.**~~ (In development so no PyPi package yet, install via GitHub instead.)
```sh
#Windows/Linux

pip install novauniverse
```
2. **That's It!** - *Brief Example Below*
```python
from novauniverse import NovaClient, Events, NovaOnlinePlayer 

client = NovaClient()

@client.on_event(Events.CLIENT_READY)
def client_is_ready():
    print("Client is ready!")

@client.on_event(Events.PLAYER_JOIN)
def on_player_join(player:NovaOnlinePlayer):
    print(f"{player.username} joined {player.server_name}!")

client.start()
```

> ### More Documentation at https://nupy.devgoldy.me/