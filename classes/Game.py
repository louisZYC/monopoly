from model.Player import Player
from model.ChanceSquare import ChanceSquare
from model.FreeParkingSquare import FreeParkingSquare
from model.GoSquare import GoSquare
from model.GoToJailSquare import GoToJailSquare
from model.InJailOrJustVisitingSquare import InJailOrJustVisitingSquare
from model.TaxSquare import TaxSquare
from model.PropertySquare import PropertySquare


class Game:
    def __init__(self, player_dict: dict = {}, square_dict: dict = {}, game_id: str = "", current_turn_index: str = ""):
        self.player_cit = player_dict
        self.square_dict = square_dict
        self.game_id = game_id
        self.current_turn_index = current_turn_index
        return

    def play(self):
        return
