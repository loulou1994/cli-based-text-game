from cli_based_game.game import Game
from cli_based_game.player import Player

def main() -> None:
    new_game = Game([], Player([]))
    print("Hello from cli-based-game!")