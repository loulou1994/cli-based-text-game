from typing import List, TypedDict, Optional, Tuple
from .lookups.world import Regions

class Destination(TypedDict):
    movements: List[str]
    to: Tuple[str, str]

class Location(TypedDict):
    name: str
    description: str
    destinations: List[Destination]
    conditions: dict[str, bool]
    region: Regions