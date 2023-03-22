Change Log
==========

v2.0 - BIG Rewrite, BREAKING CHANGES (22/03/2023)
---------------------------
- API requests are much much faster and efficient.
- BRAND NEW programming interface.
- Events are NOW HERE! (player join, player leave, client ready, etc)
- NEW and BETTER Docs! (LIVE at https://nupy.devgoldy.me/)
- Improved logging.
- Improved type hint.

v1.1a1 - New Update (23/02/2022)
---------------------------
- Significantly improved typing hint.
- Added comments to each attribute in all the novauniverse objects.
- "is_online" attribute in player object now always returns live data.
- Basic server stats have been added. >> "novauniverse.Server()"
- License key validation has been added. >> "novauniverse.License()"
- Switched to using the internal mojang API.

v1.0a1 - First Alpha Release (02/01/2022)
---------------------------
- "novauniverse.player()" is now "novauniverse.Player()" and same goes with "novauniverse.session()", more info in documentation. Docs: https://novauniversepy.readthedocs.io/en/latest/#
- Extended support down untill python 3.7. So api wrapper will support python 3.7, 3.8, 3.9 and above. (keep in mind python 3.10 has not tested yet but may work perfectly)