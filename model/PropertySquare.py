from model.Square import Square
from model.Player import Player


class PropertySquare(Square):
    def __init__(self, token: int = 0, rents: int = 0, price: int = 0, name: str = "", owner: Player = None):
        super().__init__(token)
        self.rents = rents
        self.price = price
        self.name = name
        self.owner = owner

    def action(self, player_controller, square_controller):
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

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_has_owner(self):
        return self.owner != None

    def remove_owner(self):
        self.owner = None
