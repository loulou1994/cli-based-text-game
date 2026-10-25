from typing import List
from abc import abstractmethod, ABC

from cli_based_game.lookups.hints import Hint_Locations

N_HINTS = 1

class AbstractHint(ABC):
    @abstractmethod
    def show_hint(self, forest_loc: str) -> str:
        pass

    @abstractmethod
    def can_show_hint(self, forest_loc: str) -> bool:
        pass

    @property
    @abstractmethod
    def question(self) -> str:
        pass

class Forest_Hint_State():
    def __init__(self) -> None: # hint_loc: str
        # self._hint_loc = hint_loc
        self._turn_count = 0
        self._used = False

    @property
    def turn_count(self) -> int:
        return self._turn_count

    @property
    def used(self) -> bool:
        return self._used
    
    def increment_turn_count(self) -> None:
        self._turn_count += 1

class Forest_Hint_Solver(AbstractHint):
    def __init__(self, turns: int, question: str, forest_states: List[Forest_Hint_State]): # hint_name: str
        # self._hint_name = hint_name
        self._turns = turns
        self._question = question
        self._forest_states = forest_states

    def show_hint(self, forest_loc: str) -> str:
        return "Here's the solution to the forest maze!"
    
    def can_show_hint(self, forest_loc: str):
        # for location_state in locations_state[Hint_Locations.FOREST.value]:

        #     if not location_state.used and location_state.turn_count == self._turns:
        #         return True
            
        return False
    
    @property
    def question(self) -> str:
        return self._question