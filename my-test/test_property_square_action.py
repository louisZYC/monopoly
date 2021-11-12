import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/louis/Desktop/year3/software-engineering/monoplay')
from classes.Game import Game
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController
from model.Player import Player
from model.PropertySquare import PropertySquare
from view.PlayerView import PlayerView
from view.SquareView import SquareView

square_view = SquareView()
player_view = PlayerView()
square_controller = SquareController(square_view)
player_controller = PlayerController(player_view)
target_square = PropertySquare(1, 150, 300, 'Tai O')
ed = Player('ed', 1500, 1, -1)
louis = Player('louis', 1500, 1, -1)

player_controller.set_target_player(ed)
square_controller.set_target_square(target_square)
target_square.action(player_controller, square_controller)
player_controller.set_target_player(louis)
target_square.action(player_controller, square_controller)

print('{}: {}, {}: {}'.format(
    ed.get_name(),
    ed.get_money(),
    louis.get_name(),
    louis.get_money()
))
