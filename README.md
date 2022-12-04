# Nova Universe.py *(Rewrite)*

[![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)](https://discord.gg/4gZSVJ7)
[![PyPI version](https://badge.fury.io/py/novauniverse.svg)](https://pypi.org/project/novauniverse/)
[![Python Badge](https://img.shields.io/pypi/pyversions/GoldyBot?style=flat)](https://pypi.org/project/novauniverse/ "Supported python versions.")
[![Docs Badge](https://img.shields.io/static/v1?label=docs&message=Available&color=light-green)](https://novauniversepy.devgoldy.me/)

<p align="center">
 <img src="https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png" width="500" />
</p>

### ``novauniverse.py`` - A modern API wrapper for the minecraft server Nova Universe written in Python.

<p align="right">
 <img align="left" src="./assets/logo.png" width="180" />
 
 # *What is Nova Universe.py?*
 NovaUniverse.py is a API wrapper for the minecraft server **[Nova Universe](https://novauniverse.net/)** that allows you to access the Nova Universe [API](https://novauniverse.net/api) in a fast object oriented way in Python. One of the bonuses is that it was developed by one of the devs at NovaUniverse.
</p>

<br>

## *Install/Set Up*
1. **Install package from pip.**
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

# *Documentation*

### Documentation has been moved to: 