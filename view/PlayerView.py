from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from model.Player import Player


class PlayerView:
    def __init__(self):
        return

    def render(self, player: Player):
        result = '{}) money: {}, is in jail:{}'.format(player.get_name(), player.get_money(), player.get_is_in_jail());
        print(result)
        return
