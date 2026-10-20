from typing import List, Literal
from .hint_location_state import Forest_Hint_State

type Hints = Literal["FOREST"] | Literal["None"]

type List_Of_Hint_States = List[List[Forest_Hint_State]]

from .hints import ForestHint

type List_Of_Hints = List[ForestHint]