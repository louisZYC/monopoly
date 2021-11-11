from model.Player import Player
from model.PropertySquare import PropertySquare
from model.Square import Square


class SquareView:
    def __init__(self):
        return

    def render(self, square: Square):
        if(type(square) is PropertySquare):
            owner_obj: Player = square.get_owner()
            owner_name = 'None' if owner_obj == None else owner_obj.get_name()
            result = '{} {}) name: {}, owner: {}, price: {}, rents: {}'.format(
                square.get_token(),
                square.to_string(),
                square.get_name(),
                owner_name,
                square.get_price(),
                square.get_rents()
            )
        else:
            result = '{} {})'.format(
                square.get_token(),
                square.to_string(),
            )
        print(result)
        return
