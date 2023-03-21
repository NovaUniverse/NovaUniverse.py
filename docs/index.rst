.. NovaUniverse.py documentation master file, created by
   sphinx-quickstart on Sun Mar 19 23:26:10 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

🐍 novauniverse.py
=====================
A modern & maintained wrapper for the `Nova Universe API`_ written in Python.

.. _Nova Universe API: https://novauniverse.net/api/

.. toctree::
   :maxdepth: 1

   api
   interfaces
   objects


What is NovaUniverse.py?
==========================
NovaUniverse.py is a API wrapper for "Nova Universe" (minecraft event hosting group) that allows you to interface with the Nova Universe `API`_ in a fast object oriented way natively within Python. 
One of the bonuses is that it was developed by `ME`_, an admin at NovaUniverse.

.. _API: https://novauniverse.net/api
.. _ME: https://github.com/THEGOLDENPRO


⚙ *Install/Set Up:*
-------------------
1. **Install package from pypi.** (In development so no PyPi package yet, install via GitHub instead.)::

      #Windows/Linux

      pip install git+https://github.com/NovaUniverse/NovaUniverse.py.git@v2

2. **That's It!** - *Brief Example Below*::

      from novauniverse import NovaClient, Events, NovaOnlinePlayer 

      client = NovaClient()

      @client.on_event(Events.CLIENT_READY)
      def client_is_ready():
         print("Client is ready!")

      @client.on_event(Events.PLAYER_JOIN)
      def on_player_join(player:NovaOnlinePlayer):
         print(f"{player.username} joined {player.server_name}!")

      client.start()


*Examples:*
===============
Some brief examples of how you can use NovaUniverse.py. 🌟


The Interface ✨
==================
The easiest way to retrieve data from the Nova api using NovaUniverse.py is by using the interfaces available to you. As of March 2023, this api wrapper covers some of the novauniverse api's endpoints with an interface.

   **Here's a quick showcase on how to use them.**

   Getting Discord Stats::

      from novauniverse import Discord

      # Get discord server stats.
      discord_stats = Discord().get_stats()

      # Prints out the member count.
      print(f"There are {discord_stats.member_count.members} members on the Nova Universe discord server.")

   Getting Newsletters::

      from novauniverse import News

      # Get latest newsletter.
      latest_newsletter = News().get_latest()

      # Print it.
      print(f"The url for the news letter '{latest_newsletter.title}' is '{latest_newsletter.full_url}'.")

   Getting online players::

      from novauniverse import Server

      # Get all online players on the minecraft server.
      online_players = Server().get_online_players()

      # Print all online players on the minecraft server.
      for player in online_players:
         print(f"{player.username} is online on the '{player.server_name}' server.")

   Getting tournament results::

      from novauniverse import NovaGames, MCF

      # Get the latest Nova Games tournament.
      nova_games = NovaGames().get_latest()

      # Prints out how much each player scored in that tournament and also how many kills they achieved.
      for player in nova_games.players:
         print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the Nova Games hosted on {nova_games.date.date()}.")
      
   MCF interface also exists this same way.

   Neat right 😁.

The Search interface 🔎
=========================
Some interfaces/endpoints obtain search features, specially those that inherited from SearchInterface.

   Here we are searching by id::

      from novauniverse import News, Search

      newsletter = News().search(Search(id=17))

      print(f"Name of news letter --> {newsletter.name}")
      print(f"ID of news letter --> {newsletter.id}")

   Here we are searching by name::

      from novauniverse import News, Search

      newsletter = News().search(Search(name="Api Wrappers"))

      print(f"Name of news letter --> {newsletter.name}")
      print(f"ID of news letter --> {newsletter.id}")


   ❗ Notice!
   Each interface supports it's own SearchBy options. For example News() might support searching by id but not support searching by name. If this is the case ``novauniverse.utils.search.SearchNotCompletelySupported`` will be raised.

   More examples::
   
      from novauniverse import MCF, Search

      mcf = MCF().search(Search(id=17))

      for player in mcf.players:
         print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the MCF hosted on {mcf.date.date()}.")

   If you would like more help, you may open a Github issue or help ticket on the NovaUniverse Discord.

Events 🎟
=========
NovaUniverse.py being a feature rich api wrapper provides a collection of events that can be triggered by an action occurring on the Nova Universe Network. Like example a player joining the minecraft server.

   This is how we register a player join event::

      from novauniverse import NovaClient, Events, NovaOnlinePlayer 

      client = NovaClient()

      @client.on_event(Events.PLAYER_JOIN)
      def on_player_join(player:NovaOnlinePlayer):
         print(f"{player.username} joined {player.server_name}!")

      client.start()

   If you would like to know the attributes of NovaOnlinePlayer, check this out: `NovaOnlinePlayer`_.

   .. _NovaOnlinePlayer: https://nupy.devgoldy.me/NovaUniverse.py/interfaces.stats.server.html#novauniverse.interfaces.stats.server.nova_online_player.NovaOnlinePlayer


Configuration Reference
-------------------------
.. automodule:: novauniverse.configuration
   :members:
   :undoc-members:
   :show-inheritance:

Errors Reference
-----------------
.. automodule:: novauniverse.errors
   :members:
   :undoc-members:
   :show-inheritance:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
