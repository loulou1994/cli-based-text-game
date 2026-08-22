from typing import List
from cli_based_game.game_types import Destination
from cli_based_game.game_data import motions, actions
from cli_based_game.game_data_lookups import Motions, Actions
from enum import Enum, auto

class Player_State(Enum):
    WALKING = 1
    SPEAKING = auto()
    WALKING_BACK = auto()
    # ATTACKING = 3
    # DEFENDING = 4

class Player:
    def init__(self) -> None:
        self._state = Player_State.WALKING

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

    def update_player_state(self, player_input: str):
        if player_input in actions[Actions.TALK.value]:
            self._state = Player_State.SPEAKING
            return
        
        if player_input in actions[Actions.BACK.value]:
            self._state = Player_State.WALKING_BACK
            return
        
        for motion in motions:
            if player_input in motion:
                self._state = Player_State.WALKING
                return