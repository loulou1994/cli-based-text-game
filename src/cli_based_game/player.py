from typing import List
from cli_based_game.game_types import Destination

class Player:
    def move(self, motion_input: str, destinations: List[Destination]) -> str:
        for destination in destinations:
            for movement in destination['movements']:
                if movement.startswith(motion_input):
                    return destination["to"]
                
        for motion in Player.Motions:
            if motion.startswith(motion_input):
                raise ValueError("Can't really move with that")
        
        raise ValueError("Don't really undersand that word")