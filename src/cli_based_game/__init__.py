import cli_based_game.game_data # loading game database from game_db.yaml
from cli_based_game.game import Game
from cli_based_game.player import Player, Player_State
from cli_based_game.game_data_lookups import Motions

def main() -> None:
    new_dict = dict([("forest", 10), ("noname", "nothing in")])
    test_keys = {"forests", "patroll", "noname"}
    it_exists = any(key in new_dict for key in test_keys)

    if ("forest", "nothing") in new_dict:
        print("there they are")
    # Game().run()
    # print(ArbitraryMessages(1))
    # print("Hello from cli-based-game!")