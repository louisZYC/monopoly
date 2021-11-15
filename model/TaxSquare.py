from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.PlayerController import PlayerController
    from controller.SquareController import SquareController
from model.Square import Square


class TaxSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        square_controller.render_view_you_are_here()

        # define variables
        target_player = player_controller.target_player
        result_money_before: int = None
        result_money_after: int = None

        # input
        result_money_before = target_player.get_money()
        
        # process
        player_controller.taxing()
        result_money_after = target_player.get_money()

        print('You have paid the tax. Your Balance: {}HKD => {}HKD'.format(
            result_money_before,
            result_money_after
        ))


    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def to_string(self):
        return "Tax Square"
