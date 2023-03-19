from devgoldyutils import Colours

VER = 2.0
STAGE = ("dev", 4)

VERSION = f"v{VER}-{STAGE[0]}-{STAGE[1]}" # Full version string.

PACKAGE_NAME= "NovaUniverse.py"
PACKAGE_NAME_WITH_VER = f"{PACKAGE_NAME} ({VERSION})"

LOGGER_NAME = Colours.RED.apply_to_string(PACKAGE_NAME)
"""The name of the logger. You can use this to get the logger with ``logging.getLogger()``."""

COPYRIGHT = "\nCopyright (c) 2022-present (Dev Goldy)"