Interfaces 🧩
===============================

.. toctree::
   :maxdepth: 1

   interfaces.stats.discord
   interfaces.stats.server


.. _The Interface:

The Interface ✨
------------------
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
      
   .. note::

      MCF interface also exists this same way.

   Neat right 😁.


.. _The Search Interface:

The Search interface 🔎
-------------------------
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


   .. warning::

      Each interface supports it's own SearchBy options. For example News() might support searching by id but not support searching by name. If this is the case :py:meth:`~novauniverse.utils.search.SearchNotCompletelySupported` will be raised.

   More examples::
   
      from novauniverse import MCF, Search

      mcf = MCF().search(Search(id=17))

      for player in mcf.players:
         print(f"'{player.username}' got {player.kills} kill(s) and scored {player.score} point(s) in the MCF hosted on {mcf.date.date()}.")

   .. note::

      If you would like more help, you may open a Github issue or help ticket on the NovaUniverse Discord.


Interface Reference
---------------------
.. automodule:: novauniverse.interfaces
   :members:
   :undoc-members:
   :show-inheritance:
