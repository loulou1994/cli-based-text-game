from .game_typing import *
from .game_data_lookups import *
from .game_data import * # loading game database from game_db.yaml
# from .utils import *
from .game import Game

def main() -> None:
    Game().run()
    # print(ArbitraryMessages(1))
    # print("Hello from cli-based-game!")