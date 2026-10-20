# from .types.game_map import *
# from .lookups import *
# from .exceptions import *
# from .hints import *
# from .load_data import * # loading game db from game_db.yaml
# from .utils import *
# from cli_based_game.hints import Hint_Locations
from .game import Game

def main() -> None:
    Game().run()
    # print(ArbitraryMessages(1))
    # print("Hello from cli-based-game!")