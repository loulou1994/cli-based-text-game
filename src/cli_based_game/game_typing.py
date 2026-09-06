from typing import List, TypedDict, Optional

class Destination(TypedDict):
    movements: List[str]
    to: str

class Location(TypedDict):
    description: str
    destinations: List[Destination]
    conditions: Optional[dict[str, bool]]