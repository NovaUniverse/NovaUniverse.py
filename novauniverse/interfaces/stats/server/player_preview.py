from dataclasses import dataclass, field
from typing import List

from ....objects import NovaDataclass
from ....objects.nova_player import NovaBasicPlayer

@dataclass(repr=False)
class PlayerPreview(NovaDataclass):
    data:dict = field(repr=False)

    max_preview_items:int = field(init=False)
    content:List[NovaBasicPlayer] = field(init=False)
    additional:int = field(init=False)

    def __post_init__(self):
        super().__post_init__()

        self.max_preview_items = self.get("max_preview_items")
        self.content = [NovaBasicPlayer(player) for player in self.get("content")]
        self.additional = self.get("additional")