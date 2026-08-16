from typing import List
from cli_based_game.game_types import Destination
from cli_based_game.game_data import motions
from cli_based_game.game_data_lookups import Motions

class Player:
    def move(self, motion_input: str, destinations: List[Destination]) -> str:
        for destination in destinations:
            for movement in destination['movements']:
                if motion_input in motions[Motions[movement].value]:
                    return destination["to"]

        # player moved with an incompatible motion for the list of the current destinations
        for motion in motions:
            if motion_input in motion:
                raise ValueError("Can't really move with that")


        # player moved with an invalid motion that is not in the list of motions
        raise ValueError("Don't really undersand that word")