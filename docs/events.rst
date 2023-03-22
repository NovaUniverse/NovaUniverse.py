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


.. toctree::
   :maxdepth: 1


EventClient Reference
---------------------------
.. automodule:: novauniverse.event_client
   :members:
   :undoc-members:
   :show-inheritance:


Events Reference
---------------------------
.. automodule:: novauniverse.events
   :members:
   :undoc-members:
   :show-inheritance: