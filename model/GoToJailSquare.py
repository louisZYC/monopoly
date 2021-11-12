from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.PlayerController import PlayerController
    from controller.SquareController import SquareController
    from model.Player import Player
    from model.PropertySquare import PropertySquare
from model.Square import Square


class GoToJailSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        square_controller.render_view_you_are_here()

        # define variables
        target_player: Player = player_controller.target_player
        result_days_before = None
        result_days_after = None
        result_token_before = None
        result_token_after = None

        # input
        result_token_before = target_player.get_token()
        result_days_before = target_player.get_days_in_jail()

        # proccess
        player_controller.go_to_jail()
        result_token_after = target_player.get_token()
        result_days_after = target_player.get_days_in_jail()

        # output
        result = '6. In Jail Or Just Visiting Square) <---- You get into jail. Days: {} => {}. Token: {} => {}.'.format(
            result_days_before,
            result_days_after,
            result_token_before,
            result_token_after
        )
        print(result)

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def to_string(self):
        return "Go To Jail Square"
