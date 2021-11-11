from typing import Callable
from classes.Inquirer import Inquirer
from model.Player import Player
from model.ChanceSquare import ChanceSquare
from model.FreeParkingSquare import FreeParkingSquare
from model.GoSquare import GoSquare
from model.GoToJailSquare import GoToJailSquare
from model.InJailOrJustVisitingSquare import InJailOrJustVisitingSquare
from model.TaxSquare import TaxSquare
from model.PropertySquare import PropertySquare
from view.PlayerView import PlayerView
from view.SquareView import SquareView
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController


class Game:
    def __init__(self, player_dict: dict = {}, square_dict: dict = {}, game_id: str = "", game_name: str = "", current_turn_index: int = 0, save: Callable = None):
        self.player_dict = player_dict
        self.square_dict = square_dict
        self.game_id = game_id
        self.current_turn_index = current_turn_index
        self.save = save
        self.init()
        return

    def init(self):
        self.computed_player_list = self.player_dict.keys()
        self.computed_square_list = self.square_dict.keys()
        self.computed_player_amount = len(self.computed_player_list)
        self.computed_square_amount = len(self.computed_square_list)
        if self.current_turn_index == 0:
            self.computed_round = 0
        else:
            self.computed_round = self.current_turn_index % self.computed_player_amount
        self.player_controller = PlayerController(PlayerView())
        self.sqaure_controller = SquareController(SquareView())

    def next(self):
        self.current_turn_index += 1
        self.computed_round = self.current_turn_index % self.computed_player_amount

    def play(self):
        print("Welcome")
        print(self.computed_player_list)
        return
        while(self.computed_round != 100):
            # input
            target_player: Player
            target_player = ""
            if self.current_turn_index == 0:
                target_player_id = self.computed_player_list[0]
            else:
                target_index = self.current_turn_index % self.computed_player_amount
                target_player_id = self.computed_player_list[target_index]
            target_player = self.player_dict['byId'][target_player_id]
            self.player_controller.set_target_player(target_player)
            self.player_controller.render_view()
            # checking
            can_roll_dice = False
            if(target_player.get_money() < 0):
                pass
            elif (target_player.get_is_in_jail()):
                answer_paid = Inquirer.promot_list(
                    'Pay $300 to get out of jail?',
                    ['yes', 'no']
                )
                if(answer_paid == 'yes'):
                    can_roll_dice = True
                else:
                    pass

            # process

            break
        return
