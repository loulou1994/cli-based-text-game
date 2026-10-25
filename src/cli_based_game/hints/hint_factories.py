from typing import Any

from cli_based_game.lookups.hints import Hint_Locations
from .hint_types import Hints
from .hints import Forest_Hint_Solver, Forest_Hint_State

class Hint_Solver_Factory():

    @staticmethod
    def initialize_hint(hint: Hints, data: Any):
        match hint:
            case Hint_Locations.FOREST.name:
                forest_states = [Forest_Hint_State() for _ in range(data["n_locations"])]
                return Forest_Hint_Solver(data["turns"], data["question"], forest_states)

            case _:
                raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")

        raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")
    
# class Hint_State_Factory():

#     @staticmethod
#     def initialize_hint_state(hint: Hints, data: Any):
#         match hint:
#             case Hint_Locations.FOREST.name:
#                 return Forest_Hint_State(data)

#             case _:
#                 raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")

#         raise KeyError(f"The {hint} key is not found in hint_states_map dictionary")