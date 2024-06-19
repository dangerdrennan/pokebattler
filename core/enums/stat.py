# core/enums/stat.py

from enum import Enum, auto

class Stat(Enum):
    HP = auto()
    ATTACK = auto()
    DEFENSE = auto()
    SPECIAL_ATTACK = auto()
    SPECIAL_DEFENSE = auto()
    SPEED = auto()
    ACCURACY = auto()
    EVASION = auto()
    CRIT_CHANCE = auto()
