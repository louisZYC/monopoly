from model.Square import Square

class GoSquare(Square):
    def __init__(self, token: int = 0):
        super().__init__(token)

    def action(self, player_controller, square_controller):
        return
