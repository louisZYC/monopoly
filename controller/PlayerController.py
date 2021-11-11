import random
from model.Player import Player
from view.PlayerView import PlayerView

class PlayerController:
    def __init__(self, view: PlayerView = None, target_player: Player = None):
        self.view = view
        self.target_player = target_player
        return

    def set_target_player(self, target_player: Player):
        self.target_player = target_player

    def set_view(self, view: PlayerView):
        self.view = view

    def add_money(self, money: float):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        result_money = self.target_player.get_money() + money
        self.target_player.set_money(result_money)

    def deduct_money(self, money: float):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        result_money = self.target_player.get_money() - money
        self.target_player.set_money(result_money)

    def taxing(self):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        amount = self.target_player.get_money() * 0.1
        tax = round(amount/10)*10
        result_money = self.target_player.get_money() - tax
        self.target_player.set_money(result_money)

    def gain_or_lose(self):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        is_gain = random.random() > 0.5
        money = None
        if(is_gain):
            base = random.sample(range(1, 20), 1)
            money = base[0]*10
        else:
            base = random.sample(range(1, 30), 1)
            money = base[0] * -10
        result_money = self.target_player.get_money() + money
        self.target_player.set_money(result_money)

    def go_to_jail(self):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        self.target_player.set_zero_days_in_jail()
        self.target_player.set_token(6)

    def get_out_of_jail(self):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')

        self.target_player.set_negative_days_in_jail()

    def render_view(self):
        if(self.target_player == None):
            raise RuntimeError('please call set_target_player() first')
        elif(self.view == None):
            raise RuntimeError('please call set_target_view() first')

        self.view.render(self.target_player)
