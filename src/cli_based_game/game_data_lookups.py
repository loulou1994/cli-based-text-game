from enum import Enum, auto

class Locations(Enum):
    START_GAME_LOC=auto()
    OLD_BUILDING_LOC=auto()
    LEVELEDUP_HILL_LOC=auto()

class Motions(Enum):
    NORTH=auto()
    SOUTH=auto()
    EAST=auto()
    WEST=auto()
    HOUSE=auto()
    
class ArbitraryMessages(Enum):
    NO_BACK=auto()
