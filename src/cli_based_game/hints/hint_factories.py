from typing import Any

from cli_based_game.lookups import Hint_Locations
from .hint_types import Hints
from .hint_location_state import Forest_Hint_State
from .hints import ForestHint

class Hint_State_Factory():

    @staticmethod
    def initialize_hint_state(hint: Hints, data: Any):
        match hint:
            case Hint_Locations.FOREST.name:
                return Forest_Hint_State(data)

            case _:
                raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")

        raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")

class Hint_Factory():

    @staticmethod
    def initialize_hint(hint: Hints, data: Any):
        match hint:
            case Hint_Locations.FOREST.name:
                return ForestHint(data["turns"], data["question"])

            case _:
                raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")

        raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")