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
    def __init__(self, player_dict: dict = {}, square_dict: dict = {}, uid: str = "", name: str = "", turn: int = 0, save: Callable = None):
        self.player_dict = player_dict
        self.square_dict = square_dict
        self.uid = uid
        self.name = name
        self.turn = turn
        self.save = save
        self.init()
        return

    def init(self):
        self.player_view = PlayerView()
        self.square_view = SquareView()
        self.player_controller = PlayerController(self.player_view)
        self.sqaure_controller = SquareController(self.square_view)
        self.dice_manager = DiceManager()
        self.computed_player_list = list(self.player_dict.keys())
        self.computed_square_list = list(self.square_dict.keys())
        self.computed_player_amount = len(self.computed_player_list)
        self.computed_square_amount = len(self.computed_square_list)
        self.computed_round = self.get_computed_round()

    def play(self):
        print('Welcome')
        while(self.computed_round < 100 or self.get_has_winner()):
            # input
            target_player: Player = None
            target_square: PropertySquare = None

            if self.turn == 0:
                target_player_id = self.computed_player_list[0]
            else:
                target_index = self.turn % self.computed_player_amount
                target_player_id = self.computed_player_list[target_index]
            target_player = self.player_dict[target_player_id]
            self.player_controller.set_target_player(target_player)

            # middleware
            if target_player.get_money() < 0:
                continue

            # preparing
            while True:
                answer_action = Inquirer.promot_list(
                    '\nRound{} {}) Please select an action:'.format(
                        self.computed_round+1, target_player.get_name()),
                    [
                        ('start turn', 'start'),
                        ('check all players', 'players'),
                        ('check all squares', 'squares'),
                        ('check board', 'board'),
                        ('exit','exit')
                    ]
                )
                if answer_action == 'players':
                    self.list_all_players()
                elif answer_action == 'board':
                    self.list_board()
                elif answer_action == 'squares':
                    self.list_all_squares()
                elif answer_action == 'exit':
                    exit()

                if answer_action == 'start':
                    break

            # checking
            can_go = False
            if target_player.get_is_in_jail():
                target_fine = 150
                result_money_before = None
                result_money_after = None
                result_days_before = None
                result_days_after = None

                answer_paid = Inquirer.promot_list(
                    'Pay $150 to get out of jail? Your balance:' +
                    str(target_player.get_money()),
                    ['yes', 'no']
                )
                if answer_paid == 'yes':
                    result_money_before = target_player.get_money()
                    result_days_before = target_player.get_days_in_jail()

                    self.player_controller.deduct_money(target_fine)
                    self.player_controller.get_out_of_jail()
                    result_money_after = target_player.get_money()
                    result_days_after = target_player.get_days_in_jail()
                    print('You have paid a fine of 150HKD and get out of jail. Your balance: {} => {}. Days in jail: {} => {}.'.format(
                        result_money_before,
                        result_money_after,
                        result_days_before,
                        result_days_after
                    ))

                    self.dice_manager.rolling_dice()
                    can_go = True
                else:
                    self.dice_manager.rolling_dice()
                    result_days_before = target_player.get_days_in_jail()
                    if(self.dice_manager.get_result_doubles()):
                        self.player_controller.get_out_of_jail()
                        result_days_after = target_player.get_days_in_jail()
                        print('The result is doubles, you get out of jail. Days in jail: {} => {}'.format(
                            result_days_before,
                            result_days_after
                        ))
                        can_go = True
                    else:
                        self.player_controller.target_player.add_days_in_jail_by_one()
                        result_days_after = target_player.get_days_in_jail()
                        print('The result is not doubles, you can not get out of jail. Days in jail: {} => {}'.format(
                            result_days_before,
                            result_days_after
                        ))
                        can_go = False

                if target_player.get_days_in_jail() == 3:
                    result_money_before = target_player.get_money()
                    result_days_before = target_player.get_money()
                    self.player_controller.deduct_money(150)
                    self.player_controller.get_out_of_jail()
                    result_money_after = target_player.get_money()
                    result_days_after = target_player.get_money()
                    print('You have to paid a fine of 150 HKD since it is day 3. Your Balance: {} => {}. Days in jail: {} => {}'.format(
                        result_money_before,
                        result_money_after,
                        result_days_before,
                        result_money_before
                    ))
                    can_go = True
            else:
                self.dice_manager.rolling_dice()
                can_go = True

            # proccess
            if can_go:
                sum = target_player.get_token() + self.dice_manager.get_result_total_number()
                result_token = sum % self.computed_square_amount
                if(sum > 20):
                    result_money_before = target_player.get_money()
                    self.player_controller.add_money(1500)
                    result_money_after = target_player.get_money()
                    print('You pass through Go Square and receive 1500HKD. Your Balance: {}HKD => {}HKD'.format(
                        result_money_before,
                        result_money_after
                    ))
                if(result_token == 0):
                    result_token = 20

                target_player.set_token(result_token)
                target_square = self.square_dict[result_token]
                self.sqaure_controller.set_target_square(target_square)
                target_square.action(self.player_controller,
                                     self.sqaure_controller)

            # output
            self.next()

        # result
        winner_list = self.get_winner_list()
        result = 'Winner:\n'
        for winner in winner_list:
            result += '{}) Money: {}\n'.format(
                winner.get_name(),
                winner.get_money()
            )
        print(result)
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
        self.turn += 1
        self.computed_round = self.get_computed_round()
        self.save()

    def get_computed_round(self):
        if self.turn == 0:
            return 0
        else:
            return int(self.turn / self.computed_player_amount)

    def get_has_winner(self):
        if len(self.player_dict) == 0:
            raise RuntimeError(
                'please initialize the Game instance with at least one players of player_dict')

        exist_cout = 0

        for key in self.player_dict:
            target: Player = self.player_dict[key]
            if(target.get_money() > 0):
                exist_cout += 1

        return exist_cout == 1

    def get_winner_list(self):
        if len(self.player_dict) == 0:
            raise RuntimeError(
                'please initialize the Game instance with at least one players of player_dict')

        winner_list: list[Player] = []

        for key in self.player_dict:
            target: Player = self.player_dict[key]
            if(len(winner_list) == 0):
                winner_list.append(target)
                continue
            if target.get_money() > winner_list[0].get_money():
                winner_list = [target]
            elif target.get_money() == winner_list[0].get_money():
                winner_list.append(target)

        return winner_list
