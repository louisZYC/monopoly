from __future__ import annotations
from typing import TYPE_CHECKING
from classes.Inquirer import Inquirer
if TYPE_CHECKING:
    from controller.PlayerController import PlayerController
    from controller.SquareController import SquareController
from model.Player import Player
from model.Square import Square


class PropertySquare(Square):
    def __init__(self, token: int = 0, rents: int = 0, price: int = 0, name: str = "", owner: Player = None):
        super().__init__(token)
        self.rents = rents
        self.price = price
        self.name = name
        self.owner = owner

    def action(self, player_controller: PlayerController, square_controller: SquareController):
        if(self is not square_controller.target_square):
            raise RuntimeError(
                'please call square_controller.set_target_square() first')

        square_controller.render_view_you_are_here()

        # define variables
        target_player: Player = player_controller.target_player
        target_sqaure: PropertySquare = self
        target_owner: Player = target_sqaure.get_owner()
        target_rents = target_sqaure.get_rents()
        target_price = target_sqaure.get_price()
        result_money_customer_before: int = None
        result_money_owner_before: int = None
        result_money_customer_after: int = None
        result_money_owner_after: int = None

        if(target_owner):
            # input
            result_money_customer_before = target_player.get_money()
            result_money_owner_before = target_owner.get_money()

            # process
            player_controller.deduct_money(target_rents)
            target_owner.set_money(target_owner.get_money()+target_rents)
            result_money_customer_after = target_player.get_money()
            result_money_owner_after = target_player.get_money()

            # output
            print('You have paid {}HKD to {}. Your Balance: {}HKD => {}HKD. {}\'s Balance: {}HKD => {}HKD'.format(
                target_rents,
                target_owner.get_name(),
                result_money_customer_before,
                result_money_customer_after,
                target_player.get_name(),
                result_money_owner_before,
                result_money_owner_after
            ))
        else:
            # input
            answer_has_paid = Inquirer.promot_list('Pay {} to get the ownership of {}.'.format(
                target_price,
                target_sqaure.get_name()
            ), ['yes', 'no'])

            # process
            if(answer_has_paid == 'yes'):
                result_money_customer_before = target_player.get_money()
                square_controller.set_owner(target_player)
                player_controller.deduct_money(target_price)
                result_money_customer_after = target_player.get_money()

                # output
                result = 'You got the ownership of {} by paying {}HKD. Your Balance {}HKD => {}HKD.'.format(
                    target_sqaure.get_name(),
                    target_price,
                    result_money_customer_before,
                    result_money_customer_after
                )
                print(result)

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_rents(self):
        return self.rents

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
