NovaUniverse.py
#################################
.. image:: https://user-images.githubusercontent.com/66202304/147414615-4a410681-0e02-41e3-88cd-3d28d4bf6898.png
 :width: 600
 :align: center

Install/Set Up
**************
1. **Install package from pip.**

.. code-block:: sh

       #Windows/Linux/MacOS
       
       pip install novauniverse

2. **That's It!** 

.. code-block:: python

       import novauniverse as nova

       player = nova.player(player_name="THEGOLDENPRO")

       print(player.first_join)

       #OUTPUT: 2021-01-15 19:28:32

**(MORE INFO BELOW.)**


Get Player Data
###########

Create a Player object using the :func:`novauniverse.player` function, giving a either a player ign or player uuid. (You must give one of these arguments.)

.. function:: novauniverse.player(player_name = None, player_uuid = None)


    Creates a player object of the player found.  (Note: Entering the "uuid" of the player is faster than player's ign.)

    :param player_name: The ign of the player. (e.g. THEGOLDENPRO)
    :type player_name: str
    :param player_uuid: The FULL mojang uuid of the player. (e.g 3442be05-4211-4a15-a10c-4bdb2b6060fa)
    :type player_uuid: str
    :rtype: :class:`novauniverse.objects.player`

*Example*

.. code-block:: python

       import novauniverse as nova

       player = nova.player(player_name="THEGOLDENPRO")
       print(player.name)

       #OUTPUT: THEGOLDENPRO

Player: Object
**************

.. class:: novauniverse.objects.player

When you run :func:`novauniverse.player` you get this class, also known as the "player object".

Player: Attributes
******************

Once you have created a player object using :func:`novauniverse.player`, multiple player properties are available for you to use.

.. attribute:: player.id

    The Nova Universe id of the player. (*str*).
    
    (E.g. ``14``)

.. attribute:: player.name

    The "in game name"(ign) of the player (*str*).
    
    (E.g. ``THEGOLDENPRO``)

.. attribute:: player.uuid

    The Mojang uuid of the player. (*str*).
    
    (E.g. ``3442be05-4211-4a15-a10c-4bdb2b6060fa``)

.. attribute:: player.username

    Alias of `player.name` (*str*).
    
    (E.g ``THEGOLDENPRO``)

.. attribute:: player.first_join

    Returns datetime object of date and time the player first joined the Nova Universe network. (*datetime.datetime*).
    
    (E.g ``2021-01-15 19:28:32``)

.. attribute:: player.last_join

    Returns datetime object of date and time the player last joined the Nova Universe network. (*datetime.datetime*).
    
    (E.g ``2021-12-23 14:13:38``)
    
.. attribute:: player.is_online

    Returns True/False if the player is currently present on the network. (*bool*).
    
    (E.g ``True``)

Get Session Data
#################

text
