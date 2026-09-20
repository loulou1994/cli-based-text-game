from typing import List
from enum import Enum, auto
from cli_based_game import motions, actions, Motions, Actions, Destination, InputWordNotFoundError, InputWordUnavailableError

class Player_State(Enum):
    WALKING = 1
    SPEAKING = auto()
    WALKING_BACK = auto()
    # ATTACKING = 3
    # DEFENDING = 4

class Player:
    def __init__(self) -> None:
        self._state: Player_State = Player_State.WALKING

    def move(self, motion_input: str, destinations: List[Destination]) -> str:
        lowered_input = motion_input.lower()
        
        for destination in destinations:
            for movement in destination['movements']:
                if lowered_input in motions[Motions[movement].value]:
                    return destination["to"]

        # player moved with an incompatible motion for the list of the current destinations
        for motion in motions:
            if lowered_input in motion:
                raise InputWordUnavailableError()


        # player moved with an invalid motion that is not in the list of motions
        raise InputWordNotFoundError(motion_input)

    def update_player_state(self, player_input: str):
        lowered_input = player_input.lower()

        if lowered_input in actions[Actions.TALK.value]:
            self._state = Player_State.SPEAKING
            return
        
        if lowered_input in actions[Actions.BACK.value]:
            self._state = Player_State.WALKING_BACK
            return
        
        for motion in motions:
            if lowered_input in motion:
                self._state = Player_State.WALKING
                return

        raise InputWordNotFoundError(player_input)

    @property
    def state(self):
        return self._state