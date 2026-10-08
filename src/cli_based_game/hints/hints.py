from abc import abstractmethod, ABC

from cli_based_game.lookups import Hint_Locations
from .hint_types import List_Of_Hint_States

class AbstractHint(ABC):
    @abstractmethod
    def show_hint(self, locations_state: List_Of_Hint_States) -> str:
        pass

    @abstractmethod
    def can_show_hint(self, locations_state: List_Of_Hint_States) -> bool:
        pass

    @property
    @abstractmethod
    def question(self) -> str:
        pass

class ForestMazeHint(AbstractHint):
    def __init__(self, turns: int, question: str): # hint_name: str
        # self._hint_name = hint_name
        self._turns = turns
        self._question = question

    def show_hint(self, locations_state: List_Of_Hint_States) -> str:
        return "Here's the solution to the forest maze!"
    
    def can_show_hint(self, locations_state: List_Of_Hint_States):
        for location_state in locations_state[Hint_Locations.FOREST.value]:

            if not location_state.used and location_state.turn_count == self._turns:
                return True
            
        return False
    
    @property
    def question(self) -> str:
        return self._question