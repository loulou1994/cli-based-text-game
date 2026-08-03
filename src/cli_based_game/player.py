from typing import List
from cli_based_game.game_types import Destination

class Player:
    def __init__(self, motions: List[str]) -> None:
        self.__motions = motions

    def move(self, motion_input: str, destinations: List[Destination]) -> str:
        for destination in destinations:
            for movement in destination['movements']:
                if movement.startswith(motion_input):
                    return destination["to"]
                
        for motion in self.__motions:
            if motion.startswith(motion_input):
                raise ValueError("Can't really move with that")
        
        raise ValueError("Don't really undersand that word")