from typing import Callable
from cli_based_game.lookups import Hint_Locations
from .hint_types import List_Of_Hint_States, Hints, List_Of_Hints
from .hint_exceptions import InvalidHintTypeError

class HintDispatcher:
    def __init__(self, hints: List_Of_Hints) -> None:
        self._hints = hints
        
    def check_hints(self, location_states: List_Of_Hint_States, hint: Hints) -> tuple[bool, str|None, Callable[[List_Of_Hint_States], str]|None]:

        match hint:
            case Hint_Locations.FOREST.name:
                forest_hint = self._hints[Hint_Locations.FOREST.value]
                can_show = forest_hint.can_show_hint(location_states)

                if can_show:
                    return (True, forest_hint.question, forest_hint.show_hint)

            case _:
                raise InvalidHintTypeError(hint)

        raise InvalidHintTypeError(hint)