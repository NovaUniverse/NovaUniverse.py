# Nova Universe.py *(Pythonic API Wrapper)*

![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)
[![PyPI version](https://badge.fury.io/py/novauniverse.svg)](https://pypi.org/project/novauniverse/)

<p align="center">
 <img src="https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png" width="500" />
</p>

### ``novauniverse.py`` - A modern API wrapper for the minecraft server Nova Universe written in Python.

#### ⭐[Goals of this Project.](https://github.com/NovaUniverse/NovaUniverse.py/projects/1)

<p align="right">
 <img align="left" src="https://media.discordapp.net/attachments/710019553098465320/895037951443107860/Untitled_Artwork_4_1.png" width="180" />
 
 # *What is Nova Universe.py?*
 NovaUniverse.py is a API wrapper for the minecraft server **[Nova Universe](https://novauniverse.net/)** that allows you to access player data, player's game stats and server status across the Nova Universe network all in a object oriented pythonic way.
</p>

## *Install/Set Up*
1. **Install package from pip.**
```sh
#Windows/Linux

pip install novauniverse
```
2. **That's It!** 
```python
import novauniverse as nova

player = nova.Player(player_name="THEGOLDENPRO")

print(player.first_join)

#OUTPUT: 2021-01-15 19:28:32
```

# *Documentation*

* #### [Get Player Data](https://novauniversepy.readthedocs.io/en/latest/#get-player-data)
* #### [Get Session Data](https://novauniversepy.readthedocs.io/en/latest/#get-session-data)
* #### [Get Server Info](#get-server-info)
* #### [Get License Info]()
* #### ~~[Get Player Stats]()~~ *(Coming Soon)*

###### (MORE DOCS AT [READTHEDOCS](http://novauniversepy.readthedocs.io/)) (PYPI: [INSTALL HERE](https://pypi.org/project/novauniverse/))

<br>

## *Get Server Info*

Heres how you can grab stats about our servers running on the network. You can grab stats like, the list of players online, total player count, total server count and more with novauniverse.py.

```python
novauniverse.Server()
```
### An Example
```python
import novauniverse as nova

server = nova.Server()

print(f"There are {server.player_count} players online.")
print(f"There are {server.server_count} servers online.")
print(f"It is currently {server.localtime.time} at Zeeraa's house.")

for player in server.players:
    print(f"'{player.username}' is currently online in '{player.server_name_}'.")
```

* #### Attributes
    * **``player_count:int`` -** *The amount of players on the network right now. (LIVE)*
    * **``server_count:int`` -** *The amount of servers online on the network right now. (LIVE)*
    * **``cached:bool`` -** *Has this data been cached by the API or not.*
    * **``localtime:datetime`` -** *The local time at Zeeraa's house... uMm, returns as python datetime object. (LIVE)*
    * **``timezone:str`` -** *The name of the timezone the API server is in.*
    * **``players:list[online_player]`` -** *Returns list of players online as player object.*
