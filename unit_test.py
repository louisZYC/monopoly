import abc
import unittest
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController
from view.PlayerView import PlayerView
from view.SquareView import SquareView
from model.PropertySquare import PropertySquare
from model.Player import Player
from model.Square import Square


class TestAll(unittest.TestCase):

    def test_playercontroller_set_target_player(self):
        # TARGET: PlayerController.set_target_player()
        # PURPOSE: test if it can set a player instance to player controller attribute 'target_player' ?
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)

        result_target_player = player_controller.target_player
        self.assertIs(result_target_player, player)

    def test_playercontroller_set_view(self):
        # TARGET: PlayerController.set_view()
        # PURPOSE: test if it can set a view instance to player controller attribute 'view' ?
        view = PlayerView()
        player_controller = PlayerController()
        player_controller.set_view(view)

        result_view = player_controller.view
        self.assertIs(result_view, view)

    def test_playercontroller_add_money(self):
        # TARGET: PlayerController.add_money()
        # PURPOSE: test if it can increment player money by certain amonut?
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.add_money(100)

        result_money = player.get_money()
        self.assertEqual(result_money, 1600)

    def test_playercontroller_deduct_money(self):
        # TARGET: PlayerController.deduct_money()
        # PURPOSE: test if it can deduct player money by certain amonut?
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.deduct_money(100)

        result_money = player.get_money()
        self.assertEqual(result_money, 1400)

    def test_playercontroller_taxing(self):
        # TARGET: PlayerController.taxing()
        # PURPOSE: test if it can deduct player money by 10%?
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.taxing()

        result_money = player.get_money()
        self.assertEqual(result_money, 1350)

    def test_playercontroller_gain_or_lose(self):
        # TARGET: PlayerController.gain_or_lose()
        # PURPOSE: test if it can let player gain up to 200 or lose up to 300, and the amount can be multiply by 10?
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.gain_or_lose()

        result_money = player.get_money()
        result_reminder = result_money % 10
        self.assertTrue(
            result_money <= 1700 and
            result_money >= 1200
        )
        self.assertTrue(result_reminder == 0)

    def test_playercontroller_go_to_jail(self):
        # TARGET: PlayerController.go_to_jail()
        # PURPOSE: test if it can make player days in jail 0?
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.go_to_jail()

        result_days_in_jail = player.get_days_in_jail()
        self.assertTrue(result_days_in_jail == 0)

    def test_playercontroller_get_out_of_jail(self):
        # TARGET: PlayerController.get_out_of_jail()
        # PURPOSE: test if it can make player days in jail -1?
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.get_out_of_jail()

        result_days_in_jail = player.get_days_in_jail()
        self.assertTrue(result_days_in_jail == -1)

    def test_squarecontroller_set_target_square(self):
        # TARGET: SquareController.set_target_square()
        # PURPOSE: test if it can set a square instance to square controller attribute 'target_square' ?
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)

        result_player = square_controller.target_square
        self.assertIs(result_player, square)

    def test_squarecontroller_set_view(self):
        # TARGET: SquareController.set_view()
        # PURPOSE: test if it can set a view instance to square controller attribute 'view' ?
        view = SquareView()
        square_controller = SquareController()
        square_controller.set_view(view)

        result_view = square_controller.view
        self.assertIs(result_view, view)

    def test_squarecontroller_set_owner(self):
        # TARGET: SquareController.set_owner()
        # PURPOSE: test if it can make square has owner?
        player = Player()
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)
        square_controller.set_owner(player)

        result_owner = square.get_owner()
        self.assertIs(result_owner, player)

    def test_squarecontroller_remove_owner(self):
        # TARGET: SquareController.remove_owner()
        # PURPOSE: test if it can make square remove owner?
        player = Player()
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)
        square_controller.set_owner(player)
        square_controller.remove_owner()

        result_owner = square.get_owner()
        self.assertIs(result_owner, None)


if __name__ == '__main__':
    unittest.main()
