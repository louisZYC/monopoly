from typing import Callable
from classes.DiceManager import DiceManager
from classes.Inquirer import Inquirer
from model.Player import Player
from model.ChanceSquare import ChanceSquare
from model.FreeParkingSquare import FreeParkingSquare
from model.GoSquare import GoSquare
from model.GoToJailSquare import GoToJailSquare
from model.InJailOrJustVisitingSquare import InJailOrJustVisitingSquare
from model.Square import Square
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
        self.computed_player_list = list(self.player_dict.keys())
        self.computed_square_list = list(self.square_dict.keys())
        self.computed_player_amount = len(self.computed_player_list)
        self.computed_square_amount = len(self.computed_square_list)
        if self.current_turn_index == 0:
            self.computed_round = 0
        else:
            self.computed_round = self.current_turn_index % self.computed_player_amount
        self.player_view = PlayerView()
        self.square_view = SquareView()
        self.player_controller = PlayerController(self.player_view)
        self.sqaure_controller = SquareController(self.square_view)
        self.dice_manager = DiceManager()

    def play(self):
        print("Welcome")
        while(self.computed_round < 100):
            # input
            target_player: Player = None
            target_square: PropertySquare = None
            if self.current_turn_index == 0:
                target_player_id = self.computed_player_list[0]
            else:
                target_index = self.current_turn_index % self.computed_player_amount
                target_player_id = self.computed_player_list[target_index]
            target_player = self.player_dict[target_player_id]
            self.player_controller.set_target_player(target_player)

            # middleware
            while True:
                answer_action = Inquirer.promot_list(
                    'Round{} {}) Please select an action:'.format(
                        self.computed_round+1, target_player.get_name()),
                    [
                        ('start turn', 'start'),
                        ('check all players', 'players'),
                        ('check all squares', 'squares'),
                        ('check board', 'board')
                    ]
                )
                if answer_action == 'players':
                    self.list_all_players()
                elif answer_action == 'board':
                    self.list_board()
                elif answer_action == 'squares':
                    self.list_all_squares()

                if answer_action == 'start':
                    break

            # checking
            can_go = False
            if target_player.get_money() < 0:
                pass
            elif target_player.get_is_in_jail():
                answer_paid = Inquirer.promot_list(
                    'Pay $300 to get out of jail? Your balance:' +
                    str(target_player.get_money()),
                    ['yes', 'no']
                )
                if answer_paid == 'yes':
                    self.dice_manager.rolling_dice()
                    self.player_controller.deduct_money(150)
                    self.player_controller.get_out_of_jail()
                    print('You have paid a fine of 150HKD and get out of jail. Your balance' +
                          str(target_player.get_money()))
                    can_go = True
                else:
                    self.dice_manager.rolling_dice()
                    if(self.dice_manager.get_result_doubles()):
                        self.player_controller.get_out_of_jail()
                        can_go = True
                        print('The result is doubles, you get out of jail.')
                    else:
                        self.player_controller.target_player.add_days_in_jail_by_one()
                        print(
                            'The result is not doubles, you can not get out of jail.')

                if(target_player.get_days_in_jail == 3):
                    self.player_controller.deduct_money(150)
                    self.player_controller.get_out_of_jail()
                    can_go = True
                    print('You have paid a fine of 150 HKD since you did not throw doubles by your third turn. Your Balance' +
                          str(target_player.get_money()))
            else:
                self.dice_manager.rolling_dice()
                can_go = True

            # proccess
            if can_go:
                target_token = (
                    target_player.get_token()
                    + self.dice_manager.get_result_total_number()
                ) % self.computed_square_amount
                target_player.set_token(target_token)
                target_square = self.square_dict[target_token]
                self.sqaure_controller.set_target_square(target_square)
                target_square.action(self.player_controller,self.sqaure_controller)
            # output
            self.next()
        return

    def list_all_players(self):
        for key in self.player_dict:
            target = self.player_dict[key]
            self.player_view.render(target)

    def list_all_squares(self):
        for key in self.square_dict:
            target = self.square_dict[key]
            self.square_view.render(target)

    def list_board(self):
        player_map = {}
        for key in self.player_dict:
            target: Player = self.player_dict[key]
            player_map[target.get_name()] = target.get_token()

        for key in self.square_dict:
            target: PropertySquare = self.square_dict[key]
            result = '{} {} '.format(target.get_token(), target.to_string())
            result_players = ''
            for key in player_map:
                if player_map[key] == target.get_token():
                    result_players += key+','
            if result_players != '':
                result += '<-----' + result_players
            print(result)

    def next(self):
        self.current_turn_index += 1
        self.computed_round = self.current_turn_index / self.computed_player_amount
