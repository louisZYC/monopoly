class Player:
    def __init__(self, name: str = "", money: int = 0, token: int = 0, days_in_jail: int = 0):
        self.name = name
        self.money = money
        self.token = token
        self.days_in_jail = days_in_jail

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_is_in_jail(self):
        return self.days_in_jail > -1

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def add_days_in_jail_by_one(self):
        self.days_in_jail += 1

    def get_days_in_jail(self):
        return self.days_in_jail

    def set_negative_days_in_jail(self):
        self.days_in_jail = -1

    def set_zero_days_in_jail(self):
        self.days_in_jail = 0