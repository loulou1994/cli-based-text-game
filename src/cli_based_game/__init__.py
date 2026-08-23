import cli_based_game.game_data # loading game database from game_db.yaml
from cli_based_game.game import Game
from cli_based_game.player import Player, Player_State
from cli_based_game.game_data_lookups import Motions

def main() -> None:
    Game().run()
    # print(ArbitraryMessages(1))
    # print("Hello from cli-based-game!")