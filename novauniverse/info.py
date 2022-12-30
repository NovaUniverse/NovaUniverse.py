VER = 2.0
STAGE = ("dev", 1)

VERSION = f"v{VER}-{STAGE[0]}-{STAGE[1]}" # Full version string.

PACKAGE_NAME= "NovaUniverse.py"
PACKAGE_NAME_WITH_VER = f"{PACKAGE_NAME} ({VERSION})"

LOGGER_NAME = f"\u001b[31m{PACKAGE_NAME}\u001b[0m"
"""The name of the logger. You can use this to get the logger with ``logging.getLogger()``."""

FOOTER = "\nCopyright (c) 2022-present (Dev Goldy)"