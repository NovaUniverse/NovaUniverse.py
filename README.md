[![Discord Shield](https://discordapp.com/api/guilds/692764975902752871/widget.png?style=shield)](https://discord.gg/4gZSVJ7)
[![PyPI version](https://badge.fury.io/py/novauniverse.svg)](https://pypi.org/project/novauniverse/)
[![Python Badge](https://img.shields.io/pypi/pyversions/GoldyBot?style=flat)](https://pypi.org/project/novauniverse/ "Supported python versions.")
[![Docs Badge](https://img.shields.io/static/v1?label=docs&message=Available&color=light-green)](https://novauniversepy.devgoldy.me/)

<p align="center">
 <img src="https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png" width="500" />
</p>

### [``novauniverse.py``](https://pypi.org/project/novauniverse/) - A modern & maintained wrapper for the [Nova Universe API](https://novauniverse.net/api/) written in Python.

#### ℹ Notice: 2.0 is currently in development so PyPi package install will not be avaliable but you can still install it via github. More on that below.

<p align="right">
 <img align="left" src="https://raw.githubusercontent.com/NovaUniverse/NovaUniverse.py/v2/assets/logo.png" width="180" />
 
 <h2>What is Nova Universe.py?</h2>
 NovaUniverse.py is a API wrapper for the minecraft server <a href="https://novauniverse.net/">Nova Universe</a> that allows you to access the Nova Universe <a href="https://novauniverse.net/api">API</a> in a fast object oriented way in Python. One of the bonuses is that it was developed by one of the devs at NovaUniverse.
</p>

<br>

<details>
  <summary> <b>📔 Menu</b> </summary>
  
- ### [*Install/Set Up*](#installset-up)
- ### [*Examples*](#examples)
  - [The Interface](#the-interface)
  - [The Search interface](#the-search-interface)
  - [Events](#events)

</details>

<br>

## *Install/Set Up*
1. ~~**Install package from pypi.**~~ (In development so no PyPi package yet, install via GitHub instead.)
```sh
#Windows/Linux

pip install git+https://github.com/NovaUniverse/NovaUniverse.py.git@v2
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

## *Examples*
Some brief examples of how you can use NovaUniverse.py.

- ### The Interface
    The easiest way to retrieve data from the Nova api using NovaUniverse.py is by using the interfaces available to you. As of December 2022, this api wrapper covers most of the api's endpoints with an interface.

    Here's a quick showcase on how to use them.

    - Getting Discord Stats.

        ```python
        from novauniverse import Discord

        # Get discord server stats.
        discord_stats = Discord().get_stats()

        # Prints out the member count.
        print(f"There are {discord_stats.member_count.members} members on the Nova Universe discord server.")
        ```
    - Getting Newsletters.

        ```python
        from novauniverse import News

        # Get latest newsletter.
        latest_newsletter = News().get_latest()

        # Print it.
        print(f"The url for the news letter '{latest_newsletter.title}' is '{latest_newsletter.full_url}'.")
        ```
    - Getting online players.

        ```python
        from novauniverse import Server

        # Get all online players on the minecraft server.
        online_players = Server().get_online_players()

        # Print all online players on the minecraft server.
        for player in online_players:
            print(f"{player.username} is online on the '{player.server_name}' server.")
        ```

    - Getting tournament results.

        ```python
        from novauniverse import NovaGames, MCF

        # Get the latest Nova Games tournament.
        nova_games = NovaGames().get_latest()

        # Prints out how much each player scored in that tournament and also how many kills they achieved.
        for player in nova_games.players:
            print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the Nova Games hosted on {nova_games.date.date()}.")
        ```
        
        MCF interface also exists this same way.

    Neat right 😁, more info in our [docs](https://novauniversepy.devgoldy.me/).

- ### The Search interface

    Some interfaces/endpoints obtain search features, specially those that inherited from SearchInterface.

    Here we are searching by id.
    ```python
    from novauniverse import News, Search

    newsletter = News().find(Search(id=17))

    print(f"Name of news letter --> {newsletter.name}")
    print(f"ID of news letter --> {newsletter.id}")
    ```

    Here we are searching by name.
    ```python
    from novauniverse import News, Search

    newsletter = News().find(Search(name="Api Wrappers"))

    print(f"Name of news letter --> {newsletter.name}")
    print(f"ID of news letter --> {newsletter.id}")
    ```

    #### ❗ Notice!
    Each interface supports it's own SearchBy options. For example News() might support searching by id but not support searching by name. If this is the case ``novauniverse.utils.search.SearchNotCompletelySupported`` will be raised.

    More examples...
    ```python
    from novauniverse import MCF, Search

    mcf = MCF().find(Search(id=17))

    for player in mcf.players:
        print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the MCF hosted on {mcf.date.date()}.")
    ```

- ### Events
    NovaUniverse.py being a feature rich api wrapper provides a collection of events that can be triggered by an action occurring on the Nova Universe Network. Like example a player joining the minecraft server.

    This is how we register a player join event.
    ```python
    from novauniverse import NovaClient, Events, NovaOnlinePlayer 

    client = NovaClient()

    @client.on_event(Events.PLAYER_JOIN)
    def on_player_join(player:NovaOnlinePlayer):
        print(f"{player.username} joined {player.server_name}!")

    client.start()
    ```

    If you would like to know the attributes of NovaOnlinePlayer, check this out: [**NovaOnlinePlayer**](https://novauniversepy.devgoldy.me/novauniverse/interfaces/stats/server/nova_online_player.html#NovaOnlinePlayer)

