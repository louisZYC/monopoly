import sys
sys.path.insert(1, '/home/louis/Desktop/year3/software-engineering/monopoly')
from classes.Game import Game
from classes.GameManager import GameManager
from classes.DbApi import DbApi
from model.Player import Player
from model.ChanceSquare import ChanceSquare
from model.FreeParkingSquare import FreeParkingSquare
from model.GoSquare import GoSquare
from model.GoToJailSquare import GoToJailSquare
from model.InJailOrJustVisitingSquare import InJailOrJustVisitingSquare
from model.TaxSquare import TaxSquare
from model.PropertySquare import PropertySquare


game_manager = GameManager()

game_manager.games = DbApi.READ_JSON('./data/game.json')
game_manager.game_list = game_manager.games['byId']
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
for key in range(2):
    target_name = 'player' + str(key)
    player_dict[target_name] = Player(target_name, 1500, 1, -1)
game_manager.game = Game(
    player_dict,
    square_dict,
    'abcdefghijklmn',
    'game_name',
    0,
    game_manager.save
)
game_manager.save()
        