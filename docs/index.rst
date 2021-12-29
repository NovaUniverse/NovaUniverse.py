NovaUniverse.py
###############

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
###############

To grab player data you got to create a Player object using the :func:`novauniverse.player` function by giving it either a player ign or player uuid. **(You must feed one of these arguments.)**

.. function:: novauniverse.player(player_name = None, player_uuid = None)


    Creates a player object of the player found.  **(Note: Using the "player_uuid" argument is faster than using the "player_name" argument to find a player.)**

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

    The Nova Universe id of the player. (*str*)
    
    (E.g. ``14``)

.. attribute:: player.name

    The "in game name"(ign) of the player. (*str*)
    
    (E.g. ``THEGOLDENPRO``)

.. attribute:: player.uuid

    The Mojang uuid of the player. (*str*)
    
    (E.g. ``3442be05-4211-4a15-a10c-4bdb2b6060fa``)

.. attribute:: player.username

    Alias of ``player.name``. (*str*)
    
    (E.g ``THEGOLDENPRO``)

.. attribute:: player.first_join

    Returns datetime object of date and time the player first joined the Nova Universe network. (*datetime.datetime*)
    
    (E.g ``2021-01-15 19:28:32``)

.. attribute:: player.last_join

    Returns datetime object of date and time the player last joined the Nova Universe network. (*datetime.datetime*)
    
    (E.g ``2021-12-23 14:13:38``)
    
.. attribute:: player.is_online

    Returns True/False if the player is currently present on the network. (*bool*)
    
    (E.g ``True``)

.. attribute:: player.sessions

    Returns list of sessions the player was in as player session objects(:class:`novauniverse.objects.player_session`). (*list*)
    
    (E.g ``[<novauniverse.objects._player_.player.player_session object at ...>, <novauniverse.objects._player_.player.player_session object at >...``)

Get Session Data
#################

To grab full game session data you can create a session object using the :func:`novauniverse.session` function by passing in the id of the session to find.

.. function:: novauniverse.session(session_id:str)


    Creates a session object of the session found.  **(Note: You can also access sessions from** :class:`novauniverse.objects.player` **of the games that the player has played.)**

    :param session_id: The id of the session. (e.g. ``95``)
    :type player_name: str

    :rtype: :class:`novauniverse.objects.session`

*Example*

.. code-block:: python

       import novauniverse as nova

       session = nova.session(session_id="95")
       print(session.game.name)

       #OUTPUT: Missile Wars

Session: Object
**************

.. class:: novauniverse.objects.session

When you run :func:`novauniverse.session` you get this class, also known as the "session object" or "game session object".

Session: Attributes
******************

Once you have created a session object using :func:`novauniverse.session`, multiple session properties are available for you to use.

.. attribute:: session.game

    Returns a game object(:class:`novauniverse.objects.game`). (*novauniverse.objects.game*)

    **(NOTICE: Check out** :class:`novauniverse.objects.game` **to find out how to grab the session's game "name" and "code name".)**
    
    (E.g. ``<novauniverse.objects._game_.game object at ...>``)

.. attribute:: session.id

    The id of the session. (*int*)
    
    (E.g. ``95``)

.. attribute:: session.metadata

    The metadata of the session's game. (*str*)
    
    (E.g. ``1,2,RED``)

.. attribute:: session.total_places

    The total amount of placement slots in the session's game. (*int*)
    
    (E.g ``2``)

.. attribute:: session.datetime

    Returns python datetime object of the date and time the session's game was created. (*datetime.datetime*)
    
    (E.g ``2021-12-20 14:03:33``)

.. attribute:: session.timestamp

    Alias of ``session.timestamp``. (*datetime.datetime*)
    
    (E.g ``2021-12-20 14:03:33``)
    
.. attribute:: session.players

    Returns list of players who were in the session's game as basic player objects(:class:`novauniverse.objects.basic_player`). (*list*).
    
    (E.g ``[<novauniverse.objects._player_.basic_player object at ...>, <novauniverse.objects._player_.basic_player object at ...>, <novauniverse.objects._player_.basic_player object at ...>]``)


Game: Object
************

.. class:: novauniverse.objects.game

When you use property ``session.game`` you get this class. The game class contains data like game "name" and "code name". More info below.

Game: Attributes
****************

.. attribute:: game.name

    The display name of the session's game. (*str*)
    
    (E.g. ``Missile Wars``)

.. attribute:: game.code_name

    The code name of the session's game. (*str*)
    
    (E.g. ``missilewars``)

.. attribute:: game.display_name

    Alias of ``game.name``. (*str*)
    
    (E.g. ``Missile Wars``)