from typing import Callable, Tuple

from cli_based_game.types.game_hints import List_Of_Hint_States, Hints
from cli_based_game.lookups import Hint_Locations
from .hints import ForestMazeHint

class HintDispatcher:
    def __init__(self, hints: Tuple[ForestMazeHint]) -> None:
        self._hints = hints
        
    def check_hints(self, locations_state: List_Of_Hint_States, hint: Hints) -> tuple[bool, str|None, Callable[[List_Of_Hint_States], str]|None]:

        match hint:
            case Hint_Locations.FOREST.name:
                forest_maze_hint = self._hints[Hint_Locations.FOREST.value]
                can_show = forest_maze_hint.can_show_hint(locations_state)

                if can_show:
                    return (True, forest_maze_hint.question, forest_maze_hint.show_hint)

            case "None":
                # here might be another hint solver
                pass

        return (False, None, None)