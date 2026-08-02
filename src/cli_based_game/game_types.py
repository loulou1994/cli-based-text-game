from typing import List, TypedDict

class Destination(TypedDict):
    movements: List[str]
    to: str

class Location(TypedDict):
    description: str
    destinations: List[Destination]