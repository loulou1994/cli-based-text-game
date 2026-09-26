from typing import List, TypedDict, Literal, Tuple

from .game_hints.locations_hints_state import Forest_Loc_State

class Destination(TypedDict):
    movements: List[str]
    to: str

class Location(TypedDict):
    description: str
    destinations: List[Destination]
    conditions: dict[str, bool]

type Hint = Literal["FOREST"] | Literal["None"]
type List_Of_Hint_States = Tuple[List[Forest_Loc_State]]
