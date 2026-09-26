from typing import Callable, Tuple

from . import ForestMazeHint
from .. import List_Of_Hint_States, Hint, Hints

class HintDispatcher:
    def __init__(self, hints: Tuple[ForestMazeHint]) -> None:
        self._hints = hints

    def check_hints(self, locations_state: List_Of_Hint_States, hint: Hint) -> tuple[bool, str|None, Callable[[List_Of_Hint_States], str]|None]:

        match hint:
            case Hints.FOREST.name:
                forest_maze_hint = self._hints[Hints.FOREST.value]
                can_show = forest_maze_hint.can_show_hint(locations_state)

                if can_show:
                    return (True, forest_maze_hint.question, forest_maze_hint.show_hint)

            case "None":
                # here might be another hint solver
                pass

        return (False, None, None)