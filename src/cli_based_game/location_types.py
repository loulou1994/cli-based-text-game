from typing import List, TypedDict

class Destination(TypedDict):
    movements: List[str]
    to: str

class Location(TypedDict):
    name: str
    description: str
    destinations: List[Destination]
    conditions: dict[str, bool]