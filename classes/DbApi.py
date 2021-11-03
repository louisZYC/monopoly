import json

class DbApi:

    def __init__(self):
        return

    def READ_JSON(self, gameId):
        f = open('./data/game.json')
        games = json.load(f)
        f.close()
        return games['byId'][gameId]

    def WRITE_JSON(self,game):
        f = open('./data/game.json')
        games = json.load(f)
        f.close()
        
        gameId = game['id']
        games['byId'][gameId] = game
        allIds = []
        for key in games['byId']:
            allIds.append(key)
        games['allIds'] = allIds
        f = open('./data/game.json', 'w')
        f.write(json.dumps(games))
        f.close()
        
