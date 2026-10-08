from typing import List, Literal

type Hints = Literal["FOREST"] | Literal["None"]

from .hint_location_state import Forest_Hint_State

type List_Of_Hint_States = List[List[Forest_Hint_State]]