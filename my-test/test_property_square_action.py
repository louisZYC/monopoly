import sys
sys.path.insert(1, '/home/louis/Desktop/year3/software-engineering/monopoly')
from view.SquareView import SquareView
from view.PlayerView import PlayerView
from model.PropertySquare import PropertySquare
from model.Player import Player
from controller.SquareController import SquareController
from controller.PlayerController import PlayerController
from classes.Game import Game


ed = Player('ed', 1500, 1, -1)
louis = Player('louis', 1500, 1, -1)
square = PropertySquare(12, 75, 700, 'Tai O')
player_view = PlayerView()
player_controller = PlayerController(player_view)
square_view = SquareView()
square_controller = SquareController(square_view)

player_controller.set_target_player(ed)
square_controller.set_target_square(square)
square.action(player_controller, square_controller)

player_controller.set_target_player(louis)
square.action(player_controller, square_controller)
