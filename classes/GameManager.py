from random import choices
import inquirer
import json
from classes.DbApi import DbApi
from classes.Game import Game


class GameManager:
    def __init__(self):
        self.dbAPi = DbApi()
        self.games = None
        return

    def init(self):
        return

    def load(self, gameId):

        return

    def save(self):
        return

    def run(self):
        self.games = json.load(open('./data/game.json'))
        choices = self.games['byId']
        questions = [
            inquirer.List('targetGameId',
                          message="What size do you need?",
                          choices=['Jumbo', 'Large', 'Standard',
                                   'Medium', 'Small', 'Micro'],
                          ),
        ]

        # answers = inquirer.prompt(questions)
        print(choices)
        return
