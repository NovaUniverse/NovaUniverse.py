from novauniverse import objects

from dataclasses import dataclass

@dataclass(repr=False)
class MCFTournament(objects.NovaBasicTournament):
    """An individual 🔥mcf tournament."""
    ...