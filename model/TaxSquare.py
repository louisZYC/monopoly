from model.Square import Square
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController

class TaxSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller: PlayerController, square_controller:SquareController):
        player_controller.taxing()
