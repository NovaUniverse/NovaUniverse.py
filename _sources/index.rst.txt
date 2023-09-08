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
   events
   interfaces
   objects
   utils


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

      pip install novauniverse

2. **That's It!** - *Brief Example Below*::

      from novauniverse import EventClient, Events, NovaOnlinePlayer 

      client = EventClient()

      @client.on_event(Events.CLIENT_READY)
      def client_is_ready():
         print("Client is ready!")

      @client.on_event(Events.PLAYER_JOIN)
      def on_player_join(player: NovaOnlinePlayer):
         print(f"{player.username} joined {player.server_name}!")

      client.start()


*Examples:*
===============
Some quick short examples to get started with NovaUniverse.py. 🌟
After you have a read here please do check out

   This is what we call interfaces. Interfaces are used to... well... **interface!** ha ha, yes... they are how you interface with the Nova Universe API.

   Getting tournament results::

      from novauniverse import NovaGames, MCF

      # Get the latest Nova Games tournament.
      nova_games = NovaGames().get_latest()

      # Prints out how much each player scored in that tournament and also how many kills they achieved.
      for player in nova_games.players:
         print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the Nova Games hosted on {nova_games.date.date()}.")

   Neat right 😁.

   .. note::

      Learn more about interfaces :ref:`over here. <The Interface>`

---------------

   Searching for a specific mcf tournament::
   
      from novauniverse import MCF, Search

      mcf = MCF().search(Search(id=17))

      for player in mcf.players:
         print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the MCF hosted on {mcf.date.date()}.")

   .. note::

      More at :ref:`search interfaces. <The Search Interface>`


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
