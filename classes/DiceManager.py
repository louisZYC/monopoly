from random import randint


class DiceManager:
    def __init__(self):
        self.total_number = 0
        self.isDoubles = False
        return

    def rolling_dice(self):
        result_1 = randint(1,4)
        result_2 = randint(1,4)
        print("The first dice gets a number",result_1)
        print("The second dice gets a number",result_2)
        self.total_number = result_1 + result_2
        self.isDoubles = result_1 == result_2
        return

    def get_result_total_number(self):
        return self.total_number

    def get_result_doubles(self):
        return self.isDoubles
