from enum import Enum, auto

class Locations(Enum):
    START_GAME_LOC=0
    OLD_BUILDING_LOC=auto()
    LEVELEDUP_HILL_LOC=auto()

class Motions(Enum):
    NORTH=0
    SOUTH=auto()
    EAST=auto()
    WEST=auto()
    HOUSE=auto()

class Actions(Enum):
    TALK=0
    BACK=auto
    # ATTACK=auto()
    # DEFEND=auto()
    
class ArbitraryMessages(Enum):
    WELCOME_MSG=0
    NO_BACK=auto()