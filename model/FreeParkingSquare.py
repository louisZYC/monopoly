from controller.PlayerController import PlayerController
from controller.SquareController import SquareController
from model.Square import Square


class FreeParkingSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        return
