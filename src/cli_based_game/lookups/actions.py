from enum import Enum, auto

class Motions(Enum):
    NORTH=0
    SOUTH=auto()
    EAST=auto()
    WEST=auto()
    ENTER=auto()
    OUT=auto()
    HOUSE=auto()
    

class Actions(Enum):
    TALK=0
    BACK=auto()
    # ATTACK=auto()
    # DEFEND=auto()