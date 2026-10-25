from typing import Literal, TypedDict
from .hints import Forest_Hint_Solver

type Hints = Literal["FOREST"] | Literal["None"]

# type List_Of_Hint_Solvers = List[Forest_Hint_Solver]

class List_Of_Hint_Solvers(TypedDict):
    FOREST: Forest_Hint_Solver
# type List_Of_Hint_States = List[List[Forest_Hint_State]]