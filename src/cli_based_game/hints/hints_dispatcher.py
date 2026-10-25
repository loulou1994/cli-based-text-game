from typing import Callable
from cli_based_game.lookups.hints import Hint_Locations
from .hint_types import Hints, List_Of_Hint_Solvers
from .hint_exceptions import InvalidHintTypeError

class HintDispatcher:
    def __init__(self, hints: List_Of_Hint_Solvers) -> None:
        self._hints = hints
        
    def check_hints(self, game_state: str, hint: Hints) -> tuple[bool, str|None, Callable[[str], str]|None]:
        hint_solver = self._hints.get(game_state)

        if (hint_solver is None):
            raise InvalidHintTypeError(hint)
        
        hint_solver.can_show_hint(game_state)
        
        # match hint:
        #     case Hint_Locations.FOREST.name:
        #         forest_hint = self._hints[Hint_Locations.FOREST.value]
        #         can_show = forest_hint.can_show_hint(game_state)

        #         if can_show:
        #             return (True, forest_hint.question, forest_hint.show_hint)

        #     case _:
        #         raise InvalidHintTypeError(hint)

        raise InvalidHintTypeError(hint)