from random import choices
import inquirer
import json
from classes.DbApi import DbApi
from classes.Game import Game


class GameManager:
    def __init__(self):
        self.games = dict()
        self.game_list = dict()
        return

    def init(self):
        return

    def load(self, game_id):
        if(len[self.game_list] == 0):
            raise RuntimeError('please call run() first')
            
        game_obj = self.game_list[game_id]
        return game_obj

    def save(self):
        return

    def run(self):
        # input
        self.games = DbApi.READ_JSON('./data/game.json')
        self.game_list = self.games['byId']

        # process
        choices = []
        for key in self.game_list:
            target = self.game_list[key]
            choices.append((target['name'], target['id']))
        questions = [
            inquirer.List('targetGameId',
                          message="Select a saved game",
                          choices=choices
                          ),
        ]

        # output
        ans = inquirer.prompt(questions)
        game_obj = self.load(ans['targetGameId'])
        return
