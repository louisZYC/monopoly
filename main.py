from classes.Game import Game
from classes.GameManager import GameManager


def main():
    game_manager = GameManager()
    # game_manager.run()
    a = len(game_manager.game_list)
    print(a)

if __name__ == '__main__':
    main()
