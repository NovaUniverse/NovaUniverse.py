NovaUniverse.py *(API Wrapper)*
*******************************
.. image:: https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png
 :width: 600
 :align: center

Install/Set Up
==============
1. **Install package from pip.**

.. code-block:: sh

       #Windows/Linux/MacOS
       
       pip install novauniverse

2. **That's It!** 

.. code-block:: python

       import novauniverse as nova

       player = nova.find.player(player_name="THEGOLDENPRO")

       print(player.first_join)

       #OUTPUT: 2021-01-15 19:28:32

**(MORE INFO IN DOCUMENTATION.)**


Documentation
*************


Get Players
===========

Create a Player object using the :func:`nova.find.player` function, giving a either a player ign or player uuid. (You must give one of these arguments.)

.. function:: nova.find.player(player_name: str | None = None, player_uuid: str | None = None)


    Creates a player object of the player found.  (Note: Entering the "uuid" of the player is faster than player's ign.)

    :param player_name: The ign of the player. (e.g. THEGOLDENPRO)
    :type player_name: str
    :param player_uuid: The FULL mojang uuid of the player. (e.g 3442be05-4211-4a15-a10c-4bdb2b6060fa)
    :type player_uuid: str
    :rtype: :class:`novauniverse.player`

Get Game Sessions
=================

text
