import json
from classes.Util import random_id
from classes.DbApi import DbApi
from classes.Game import Game
from classes.Inquirer import Inquirer
from model.Player import Player
from model.ChanceSquare import ChanceSquare
from model.FreeParkingSquare import FreeParkingSquare
from model.GoSquare import GoSquare
from model.GoToJailSquare import GoToJailSquare
from model.InJailOrJustVisitingSquare import InJailOrJustVisitingSquare
from model.TaxSquare import TaxSquare
from model.PropertySquare import PropertySquare

class_map = {
    'ChanceSquare': ChanceSquare,
    'FreeParkingSquare': FreeParkingSquare,
    'GoSquare': GoSquare,
    'GoToJailSquare': GoToJailSquare,
    'InJailOrJustVisitingSquare': InJailOrJustVisitingSquare,
    'TaxSquare': TaxSquare,
    'PropertySquare': PropertySquare,
}


class GameManager:
    def __init__(self):
        self.games = dict()
        self.game_list = dict()
        self.game = Game()
        return

    def new_game(self):
        if(len(self.games) == 0):
            raise RuntimeError('please call run() first')

        # input
        message = 'How many players?'
        choices = [2, 3, 4, 5, 6]
        answer_number_of_players = Inquirer.promot_list(message, choices)

        # process
        square_dict = {
            1: GoSquare(1),
            2: PropertySquare(2, 90, 800, 'Central'),
            3: PropertySquare(3, 65, 700, 'Wan Chai'),
            4: TaxSquare(4),
            5: PropertySquare(5, 60, 600),
            6: InJailOrJustVisitingSquare(6),
            7: PropertySquare(7, 10, 400, 'Shek O'),
            8: PropertySquare(8, 40, 500, 'Mong Kok'),
            9: ChanceSquare(9),
            10: PropertySquare(10, 15, 400, 'Tsing Yi'),
            11: FreeParkingSquare(11),
            12: PropertySquare(12, 75, 700, 'Sha Tin'),
            13: ChanceSquare(13),
            14: PropertySquare(14, 20, 400, 'Tuen Mun'),
            15: PropertySquare(15, 25, 500, 'Taipo'),
            16: GoToJailSquare(16),
            17: PropertySquare(17, 10, 400, 'Sai Kung'),
            18: PropertySquare(18, 25, 400, 'Yuen Long'),
            19: ChanceSquare(19),
            20: PropertySquare(20, 25, 600, 'Tai O')
        }
        player_dict = {}
        for key in range(answer_number_of_players):
            target_name = 'player' + str(key)
            player_dict[target_name] = Player(target_name, 1500, 1, -1)
        game_name = Inquirer.prompt_text("give a name for this game")
        self.game = Game(
            player_dict,
            square_dict,
            random_id(),
            game_name,
            0,
            self.save
        )

        # output
        self.game.play()
        return

    def load(self):
        if(len(self.games) == 0):
            raise RuntimeError('please call run() first')

        message = 'which game you want to load?'
        choices = []
        for key in self.game_list:
            target = self.game_list[key]
            choices.append((target['name'], target['id']))
        answer_game_id = Inquirer.promot_list(message, choices)
        print('loaded', answer_game_id)

    def save(self):
        print(self.game)
        return

    def run(self):
        # data:
        self.games = DbApi.READ_JSON('./data/game.json')
        self.game_list = self.games['byId']

        # created:
        message = 'How you want to play?'
        choices = ['new game', 'load game']
        answer = Inquirer.promot_list(message, choices)
        if answer == 'new game':
            self.new_game()
        elif answer == 'load game':
            self.load()
        return
