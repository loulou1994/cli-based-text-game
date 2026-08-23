from enum import Enum, auto

class Locations(Enum):
    START_GAME_LOC=0
    OLD_BUILDING_LOC=auto()
    LEVELEDUP_HILL_LOC=auto()
    END_ROAD_LOC=auto()
    FOREST_06_LOC=auto()
    FOREST_05_LOC=auto()
    FOREST_04_LOC=auto()
    FOREST_03_LOC=auto()
    FOREST_02_LOC=auto()
    FOREST_01_LOC=auto()
    FOREST_09_LOC=auto()
    FOREST_08_LOC=auto()
    FOREST_07_LOC=auto()
    GRATE_LOC=auto()
    STREAM_ROCK_SLIT_LOC=auto()
    WATER_STREAM_LOC=auto()

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
    
class ArbitraryMessages(Enum):
    WELCOME_MSG=0
    NO_BACK=auto()