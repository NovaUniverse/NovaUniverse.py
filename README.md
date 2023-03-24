<div align="center">

  # 🐍[``novauniverse.py``](https://pypi.org/project/novauniverse/)
  
  <sub>A modern & maintained wrapper for the [Nova Universe API](https://novauniverse.net/api/) written in Python.</sub>
  
  [![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)](https://discord.gg/4gZSVJ7)
  [![PyPI version](https://badge.fury.io/py/novauniverse.svg)](https://pypi.org/project/novauniverse/)
  [![Python Badge](https://img.shields.io/pypi/pyversions/novauniverse?style=flat)](https://pypi.org/project/novauniverse/ "Supported python versions.")
  [![Docs Badge](https://img.shields.io/github/actions/workflow/status/NovaUniverse/NovaUniverse.py/documentation.yaml?label=docs)](https://nupy.devgoldy.me/)
  
</div>

> #### ℹ Notice: 2.0 is currently in development so not all api endpoints are implemented.

<p align="right">
 <img align="left" src="https://raw.githubusercontent.com/NovaUniverse/NovaUniverse.py/main/docs/_static/logo.png" width="180" />
 
 <h2>What is Nova Universe.py?</h2>
 NovaUniverse.py is an API wrapper for “<a href="https://novauniverse.net/">Nova Universe</a>” (a minecraft event hosting group) that allows you to interface with the <a href="https://novauniverse.net/api">Nova Universe API</a> in a fast object oriented way natively within Python. One of the bonuses is that it was developed by <a href="https://github.com/THEGOLDENPRO">ME</a>, an admin at NovaUniverse.
</p>

<br>

## *Install/Set Up*
1. **Install package from pypi.**
```sh
#Windows/Linux

pip install novauniverse
```
2. **That's It!** - *Brief Example Below*
```python
from novauniverse import EventClient, Events, NovaOnlinePlayer 

client = EventClient()

@client.on_event(Events.CLIENT_READY)
def client_is_ready():
    print("Client is ready!")

@client.on_event(Events.PLAYER_JOIN)
def on_player_join(player:NovaOnlinePlayer):
    print(f"{player.username} joined {player.server_name}!")

client.start()
```

<br>

> ### More Examples and Info at https://nupy.devgoldy.me/
