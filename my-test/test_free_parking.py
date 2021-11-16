import sys
sys.path.insert(1, '/home/louis/Desktop/year3/software-engineering/monopoly')
from classes.Game import Game
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController
from model.Player import Player
from model.FreeParkingSquare import FreeParkingSquare
from view.PlayerView import PlayerView
from view.SquareView import SquareView


ed = Player('ed', 1500, 1, -1)
square = FreeParkingSquare(11)
player_view = PlayerView()
player_controller = PlayerController(player_view)
square_view = SquareView()
square_controller = SquareController(square_view)

player_controller.set_target_player(ed)
square_controller.set_target_square(square)
square.action(player_controller,square_controller)
