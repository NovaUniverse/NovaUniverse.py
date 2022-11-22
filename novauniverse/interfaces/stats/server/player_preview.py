from dataclasses import dataclass, field
from typing import List

from ....objects.nova_player import NovaBasicPlayer

@dataclass
class PlayerPreview:
    __data:dict = field(repr=False)

    max_preview_items:int = field(init=False)
    content:List[NovaBasicPlayer] = field(init=False)
    additional:int = field(init=False)

    def __post_init__(self):
        self.max_preview_items = self.__data["max_preview_items"]
        self.content = [NovaBasicPlayer(player) for player in self.__data["content"]]
        self.additional = self.__data["additional"]