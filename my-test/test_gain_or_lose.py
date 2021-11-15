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

player_view = PlayerView()
player_controller = PlayerController(player_view)
ed = Player('ed', 1500, 1, -1)

player_controller.set_target_player(ed)
target_square.action(player_controller, square_controller)
player_controller.set_target_player(louis)
target_square.action(player_controller, square_controller)

print('{}: {}, {}: {}'.format(
    ed.get_name(),
    ed.get_money(),
    louis.get_name(),
    louis.get_money()
))
