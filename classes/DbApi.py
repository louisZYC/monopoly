import json

class DbApi:

    def __init__(self):
        return

    def READ_JSON(self, gameId):
        games = json.load(open('./data/game.json'))
        return games[gameId]

    def WRITE_JSON(game):
        return
