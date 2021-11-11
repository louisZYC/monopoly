from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.PlayerController import PlayerController
    from controller.SquareController import SquareController
from model.Square import Square
from model.Player import Player


class PropertySquare(Square):
    def __init__(self, token: int = 0, rents: int = 0, price: int = 0, name: str = "", owner: Player = None):
        super().__init__(token)
        self.rents = rents
        self.price = price
        self.name = name
        self.owner = owner

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        # print('This is {}'.format(square_controller.))
        if(self.get_has_owner()):
            player_controller.deduct_money(self.rents)
            player_controller.set_target_player(self.owner)
            player_controller.add_money(self.rents)
        else:
            isPurchased = input("Do you want to purchase {} by {} ? If yes, type 'yes'.".format(
                self.name, self.price))
            if(isPurchased):
                player_controller.deduct_money(self.price)
                square_controller.set_owner(player_controller.target_player)

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_rents(self):
        return self.token

    def set_rents(self, rents):
        self.rents = rents

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_has_owner(self):
        return self.owner != None

    def remove_owner(self):
        self.owner = None

    def to_string(self):
        return "Property Square"
