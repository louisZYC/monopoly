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
        # input
        self.games = json.load(open('./data/game.json'))

        # process
        game_list = self.games['byId']
        choices = []
        for key in game_list:
            target = game_list[key]
            choices.append((target['name'], target['id']))
        questions = [
            inquirer.List('targetGameId',
                          message="Select a saved game",
                          choices=choices
                          ),
        ]

        # output
        answers = inquirer.prompt(questions)
        return
