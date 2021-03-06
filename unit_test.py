import json
import unittest
from classes.DbApi import DbApi
from controller.PlayerController import PlayerController
from controller.SquareController import SquareController
from view.PlayerView import PlayerView
from view.SquareView import SquareView
from model.PropertySquare import PropertySquare
from model.Player import Player
from model.Square import Square
from classes.Game import Game


class TestAll(unittest.TestCase):

    def test_playercontroller_set_target_player(self):
        # TARGET: PlayerController.set_target_player()
        # PURPOSE: test if it can set a player instance to player controller attribute 'target_player'.
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)

        result_target_player = player_controller.target_player
        self.assertIs(result_target_player, player)

    def test_playercontroller_set_view(self):
        # TARGET: PlayerController.set_view()
        # PURPOSE: test if it can set a view instance to player controller attribute 'view'.
        view = PlayerView()
        player_controller = PlayerController()
        player_controller.set_view(view)

        result_view = player_controller.view
        self.assertIs(result_view, view)

    def test_playercontroller_add_money(self):
        # TARGET: PlayerController.add_money()
        # PURPOSE: test if it can increment player money by certain amount.
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.add_money(100)

        result_money = player.get_money()
        self.assertEqual(result_money, 1600)

    def test_playercontroller_deduct_money(self):
        # TARGET: PlayerController.deduct_money()
        # PURPOSE: test if it can deduct player money by certain amount.
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.deduct_money(100)

        result_money = player.get_money()
        self.assertEqual(result_money, 1400)

    def test_playercontroller_taxing(self):
        # TARGET: PlayerController.taxing()
        # PURPOSE: test if it can deduct player money by 10%.
        player = Player('player1', 1500)
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.taxing()

        result_money = player.get_money()
        self.assertEqual(result_money, 1350)

    def test_playercontroller_gain_or_lose(self):
        # TARGET: PlayerController.gain_or_lose()
        # PURPOSE: test if it can let player gain up to 200 or lose up to 300, and the loss amount can be multiply by 10.
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
        # PURPOSE: test if it can make player days in jail 0, indicate that the player gets into jail.
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.go_to_jail()

        result_days_in_jail = player.get_days_in_jail()
        self.assertTrue(result_days_in_jail == 0)

    def test_playercontroller_get_out_of_jail(self):
        # TARGET: PlayerController.get_out_of_jail()
        # PURPOSE: test if it can make player days in jail -1, indicate that the player gets out of jail.
        player = Player()
        player_controller = PlayerController()
        player_controller.set_target_player(player)
        player_controller.get_out_of_jail()

        result_days_in_jail = player.get_days_in_jail()
        self.assertTrue(result_days_in_jail == -1)

    def test_squarecontroller_set_target_square(self):
        # TARGET: SquareController.set_target_square()
        # PURPOSE: test if its value (an attribute 'target_square' in SquareController class) can be set to a square instance.
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)

        result_player = square_controller.target_square
        self.assertIs(result_player, square)

    def test_squarecontroller_set_view(self):
        # TARGET: SquareController.set_view()
        # PURPOSE: test if its value (an attribute 'view' in SquareController class) can be set a square controller.
        view = SquareView()
        square_controller = SquareController()
        square_controller.set_view(view)

        result_view = square_controller.view
        self.assertIs(result_view, view)

    def test_squarecontroller_set_owner(self):
        # TARGET: SquareController.set_owner()
        # PURPOSE: test if it can make a property square be owned by a player.
        player = Player()
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)
        square_controller.set_owner(player)

        result_owner = square.get_owner()
        self.assertIs(result_owner, player)

    def test_squarecontroller_remove_owner(self):
        # TARGET: SquareController.remove_owner()
        # PURPOSE: test if it can remove the owner from a property square, which means that the property square does not belong to that owner anymore.
        player = Player()
        square = PropertySquare()
        square_controller = SquareController()
        square_controller.set_target_square(square)
        square_controller.set_owner(player)
        square_controller.remove_owner()

        result_owner = square.get_owner()
        self.assertIs(result_owner, None)

    def test_dbapi_read_json(self):
        # TARGET: dbApi.READ_JSON()
        # PURPOSE: test if it can load a game from json file
        games = {
            "byId": {
                "ov9r4d0k7e": {
                    "id": "ov9r4d0k7e",
                    "name": "game1",
                    "players": {
                        "byId": {
                            "player1": {
                                "name": "player1",
                                "money": 1500,
                                "token": 1,
                                "daysInJail": -1
                            }
                        },
                        "allIds": [
                            "player1"
                        ]
                    },
                    "squarues": {
                        "byId": {
                            "1": {
                                "tokens": 1,
                                "class": "PropertySquare",
                                "price": 1000,
                                "name": "Tai O",
                                "owner": "player1",
                                "rents": 100
                            }
                        },
                        "allIds": [
                            1
                        ]
                    }
                }
            },
            "allIds": [
                "ov9r4d0k7e",
            ]
        }
        path = './data/test-game.json'

        all_ids = games['allIds']
        with open(path, 'w') as f:
            f.write(json.dumps(games))
        result_games = DbApi.READ_JSON(path)
        result_all_ids = result_games['allIds']

        self.assertTrue(result_all_ids == all_ids)

    def test_dbapi_write_json(self):
        # TARGET: dbApi.WRITE_JSON()
        # PURPOSE: test if it can write a game to json file
        games = {
            "byId": {
                "ov9r4d0k7e": {
                    "id": "ov9r4d0k7e",
                    "name": "game1",
                    "players": {
                        "byId": {
                            "player1": {
                                "name": "player1",
                                "money": 1500,
                                "token": 1,
                                "daysInJail": -1
                            }
                        },
                        "allIds": [
                            "player1"
                        ]
                    },
                    "squarues": {
                        "byId": {
                            "1": {
                                "tokens": 1,
                                "class": "PropertySquare",
                                "price": 1000,
                                "name": "Tai O",
                                "owner": "player1",
                                "rents": 100
                            }
                        },
                        "allIds": [
                            1
                        ]
                    }
                }
            },
            "allIds": [
                "ov9r4d0k7e",
            ]
        }
        path = './data/test-game.json'

        all_ids = games['allIds']
        DbApi.WRITE_JSON(path, games)
        with open(path, 'r') as f:
            result_games = json.load(f)
        result_all_ids = result_games['allIds']

        self.assertTrue(result_all_ids == all_ids)

    def test_game_get_winner_list(self):
        player_dict = {
            'player1': Player('player1', 1500),
            'player2': Player('player2', 1500),
            'player3': Player('player3', 1200)
        }
        game = Game(player_dict)
        result_winner_list = game.get_winner_list()
        result_winner_names = [winner.get_name()
                               for winner in result_winner_list]
        self.assertTrue(result_winner_names == ['player1', 'player2'])

    def test_game_get_has_winner(self):
        player_dict = {
            'player1': Player('player1', 1500),
            'player2': Player('player2', -10),
            'player3': Player('player3', -10)
        }
        game = Game(player_dict)

        result_has_winner = game.get_has_winner()
        self.assertTrue(result_has_winner == True)


if __name__ == '__main__':
    unittest.main()
