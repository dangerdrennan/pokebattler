from enum import Enum, auto

class Target(Enum):
    SINGLE_TARGET_ANY = auto()
    SINGLE_TARGET_ALLY = auto()
    SINGLE_TARGET_ENEMY = auto()
    SPREAD_TARGET_ALL = auto()
    SPREAD_TARGET_ALLY = auto()
    SPREAD_TARGET_ENEMY = auto()
    