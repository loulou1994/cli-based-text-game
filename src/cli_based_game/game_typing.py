from typing import List, TypedDict

class Destination(TypedDict):
    movements: List[str]
    to: str

class Location(TypedDict):
    description: str
    destinations: List[Destination]
    conditions: dict[str, bool]

class Location_Hint_State(TypedDict):
    hint_name: str
    turn_count: int
    used: bool