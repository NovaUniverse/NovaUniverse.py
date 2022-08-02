# Nova Universe.py *(Pythonic API Wrapper)*

[![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)](https://discord.gg/4gZSVJ7)
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
* #### [Get License Info]() *(Docs Coming Soon)*
* #### [Get Mcf Stats](#get-mcf-stats-1)
* #### ~~[Get Player Stats]()~~ *(Docs Coming Soon)*

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
    * **``player_count -> int`` -** *The amount of players on the network right now. (LIVE)*
    * **``server_count -> int`` -** *The amount of servers online on the network right now. (LIVE)*
    * **``cached -> bool`` -** *Has this data been cached by the API or not.*
    * **``localtime -> datetime`` -** *The local time at Zeeraa's house... uMm, returns as python datetime object. (LIVE)*
    * **``timezone -> str`` -** *The name of the timezone the API server is in.*
    * **``players -> list[online_player]`` -** *Returns list of players online as player object.*

<br>

## *Get MCF Stats*

Heres how you can grab stats about our tournament MCF. With novauniverse.py you can grab all staticstics of each MCF week & session. Like the kills of a player or a team.

```python
novauniverse.Mcf()
```
### An Example
```python
import novauniverse as nova

mcf_games = nova.Mcf()

for mcf in mcf_games:
    print(f"This week of mcf was hosted on [{mcf.date.date()}].")
    print(f"It was won by Team {mcf.winner_team_number}, they had a total score of {mcf.winner_team.team_score}.")
    print(f"Both {mcf.winner_team.players[0].name} and {mcf.winner_team.players[1].name} was rewarded.")
    print("")

"""
This week of mcf was hosted on [2022-04-09].
It was won by Team 9, they had a total score of 1989.
Both Wavesea and ItsNitroTiger was rewarded.

This week of mcf was hosted on [2022-04-16].
It was won by Team 5, they had a total score of 1480.
Both gummywroms and ItsNitroTiger was rewarded.

This week of mcf was hosted on [2022-04-23].
It was won by Team 2, they had a total score of 1652.
Both W0lly1 and Noahkup was rewarded.

This week of mcf was hosted on [2022-04-30].
It was won by Team 3, they had a total score of 2024.
Both AiroKun and darkleonard2 was rewarded.
"""
```

* #### Attributes
    * **``id -> int`` -** *The id of the tournament.*
    * **``date -> datetime.datetime`` -** *The date when the tournament took place.*
    * **``display_name -> str`` -** *The display name of the MCF session.*
    * **``winner_team_id -> int`` -** *The team number of the winning team.*
    * **``winner_team ->`` [``ExtendedMCFTeam``](#--extendedmcfteam) -** *Returns team object of the winning team.*
    * **``teams ->`` [``list[ExtendedMCFTeam]``](#--extendedmcfteam) -** *Returns list of all teams that played in this MCF.*

<br>

## *Objects*

### ***- ``ExtendedMCFTeam``***
**( Inherits from [``BasicMCFTeam``](#--basicmcfteam) )**
```python
novauniverse.objects._mcf_.ExtendedMCFTeam()
```

This class represents a team in the mcf tournamant.

* #### Attributes
    * **``players ->`` [``list[MCFPlayer]``](#--MCFPlayer) -** *Returns list of players in that team via MCFPlayer objects.*

<br>

### ***- ``BasicMCFTeam``***
```python
novauniverse.objects._mcf_.ExtendedMCFTeam()
```

Basic mcf team class.

* #### Attributes
    * **``team_number -> int`` -** *Returns the number of this team. WARNING: This method is slower, it is recommended to use ``MCF().winner_team_number`` whenever possible if you are finding the winner's team id.*
    * **``team_score -> int``** - Returns the total score of this team.

<br>

### ***- ``MCFPlayer``***
```python
novauniverse.objects._mcf_.MCFPlayer()
```

This class represents a player in the mcf tournamant.

* #### Attributes
    * **``id -> int``** - Returns the MCF id of the player.
    * **``has_nova_account -> bool``** - Returns True/False if the player is linked to a novauniverse account.
    * **``nova_account_name -> (str | None)``** - Returns the name of the nova universe account this player is linked to.
    * **``username -> int``** - Returns the MCF id of the player.
    * **``uuid -> str``** - Returns the player's mojang uuid.
    * **``team_number -> int``** - Returns the number of the team the player is in.
    * **``score -> int``** - Returns the total score this player achived.
    * **``kills -> int``** - Returns the amount of kills this player got.
    
-------------------
### ``Documentation is still currently being written...``
