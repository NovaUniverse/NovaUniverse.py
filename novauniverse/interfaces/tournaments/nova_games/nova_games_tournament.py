from novauniverse import objects

from dataclasses import dataclass

@dataclass(repr=False)
class NovaGamesTournament(objects.NovaBasicTournament):
    """An individual 🟥nova games tournament."""
    ...