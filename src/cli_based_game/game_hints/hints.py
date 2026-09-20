from typing import List, Callable
from abc import abstractmethod, ABC

from cli_based_game import Location_Hint_State

class AbstractHint(ABC):
    @abstractmethod
    def show_hint(self, locations_state: List[Location_Hint_State]) -> str:
        pass

    @abstractmethod
    def can_show_hint(self, locations_state: List[Location_Hint_State]) -> bool:
        pass

    @property
    @abstractmethod
    def question(self) -> str:
        pass

class ForestMazeHint(AbstractHint):
    def __init__(self, hint_name: str, turns: int, question: str):
        self._hint_name = hint_name
        self._turns = turns
        self._question = question

    def show_hint(self, locations_state: List[Location_Hint_State]) -> str:
        return "Here's the solution to the forest maze!"
    
    def can_show_hint(self, locations_state: List[Location_Hint_State]):
        for location_state in locations_state:
            if location_state["hint_name"] == self._hint_name and not location_state["used"] and location_state["turn_count"] == self._turns:
                return True

        return False
    
    @property
    def question(self) -> str:
        return self._question
    
class HintDispatcher:
    def __init__(self, hints: List[AbstractHint]) -> None:
        self._hints = hints

    def check_hints(self, locations_state: List[Location_Hint_State]) -> tuple[bool, str|None, Callable[[List[Location_Hint_State]], str]|None]:
        for hint in self._hints:
            can_show = hint.can_show_hint(locations_state)

            if can_show:
                return (True, hint.question, hint.show_hint)

        return (False, None, None)