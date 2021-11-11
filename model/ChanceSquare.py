from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.PlayerController import PlayerController
    from controller.SquareController import SquareController
from model.Square import Square


class ChanceSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        player_controller.gain_or_lose()

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def to_string(self):
        return "Chance Square"
