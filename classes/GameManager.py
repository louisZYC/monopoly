import json
from os import name
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
        self.game_dict = dict()
        self.game: Game = Game()
        return

    def new_game(self):
        if(len(self.games) == 0):
            raise RuntimeError('please call run() first')

        # input
        message = 'How many players do you prefer?'
        choices = [2, 3, 4, 5, 6]
        answer_number_of_players = Inquirer.promot_list(message, choices)

        # process
        square_dict = {
            1: GoSquare(1),
            2: PropertySquare(2, 90, 800, 'Central'),
            3: PropertySquare(3, 65, 700, 'Wan Chai'),
            4: TaxSquare(4),
            5: PropertySquare(5, 60, 600, 'Stanley'),
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
        uid = 'abcdefghijklmn'
        while(uid in self.games['allIds']):
            uid = random_id()

        # output
        self.game = Game(
            player_dict,
            square_dict,
            random_id(),
            game_name,
            0,
            self.save
        )
        self.game.play()
        return

    def load(self):
        if(len(self.games) == 0):
            raise RuntimeError('please call run() first')
        # input
        message = 'which games you want to load?'
        choices = []
        for key in self.game_dict:
            target = self.game_dict[key]
            choices.append((target['name'], target['uid']))
        answer_game_id = Inquirer.promot_list(message, choices)

        # process
        uid = self.games['byId'][answer_game_id]['uid']
        name = self.games['byId'][answer_game_id]['name']
        turn = self.games['byId'][answer_game_id]['turn']
        player_dict = {}
        square_dict = {}
        for key in self.game_dict[answer_game_id]['players']['byId']:
            target = self.game_dict[answer_game_id]['players']['byId'][key]
            player_dict[target['name']] = Player(
                target['name'],
                target['money'],
                target['token'],
                target['days_in_jail']
            )
        for key in self.game_dict[answer_game_id]['squares']['byId']:
            target = self.game_dict[answer_game_id]['squares']['byId'][key]
            if class_map[target['class']] == PropertySquare:
                owner = player_dict[target['owner']
                                    ] if target['owner'] else None
                square_dict[target['token']] = PropertySquare(
                    target['token'],
                    target['rents'],
                    target['price'],
                    target['name'],
                    owner
                )
            else:
                square_dict[target['token']] = class_map[target['class']](
                    target['token']
                )

        # output
        self.game = Game(
            player_dict,
            square_dict,
            uid,
            name,
            turn,
            self.save
        )
        self.game.play()

    def save(self):
        players = {}
        squares = {}

        for key in self.game.square_dict:
            target: PropertySquare = self.game.square_dict[key]
            if(isinstance(target, PropertySquare)):
                squares[target.get_token()] = {
                    "class": target.__class__.__name__,
                    "token": target.get_token(),
                    "rents": target.get_rents(),
                    "price": target.get_price(),
                    "owner": target.get_owner().get_name() if target.get_owner() else None,
                    "name": target.get_name()
                }
            else:
                squares[target.get_token()] = {
                    "class": target.__class__.__name__,
                    "token": target.get_token()
                }
        for key in self.game.player_dict:
            target: Player = self.game.player_dict[key]
            players[target.get_name()] = {
                "name": target.get_name(),
                "money": target.get_money(),
                "token": target.get_token(),
                "days_in_jail": target.get_days_in_jail()
            }
        game = {
            "uid": self.game.uid,
            "name": self.game.name,
            "turn": self.game.turn,
            "players": {
                "byId": players,
                "allIds": [x for x in self.game.player_dict]
            },
            "squares": {
                "byId": squares,
                "allIds": [x for x in self.game.square_dict]
            }
        }

        self.games['byId'][game['uid']] = game
        if game['uid'] not in self.games['allIds']:
            self.games['allIds'].insert(0, game['uid'])
        DbApi.WRITE_JSON('./data/game.json', self.games)
        return

    def run(self):
        # data:
        self.games = DbApi.READ_JSON('./data/game.json')
        self.game_dict = self.games['byId']

        # created:
        message = 'Which games do you want to play?'
        choices = ['new game', 'load game']
        answer = Inquirer.promot_list(message, choices)
        if answer == 'new game':
            self.new_game()
        elif answer == 'load game':
            self.load()
        return
