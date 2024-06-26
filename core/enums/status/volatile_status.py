# core/enums/volatilestatus.py

from enum import Enum, auto

## more to be implemented later

class VolatileStatus(Enum):
    CONFUSED = auto()
    PROTECTED = auto()
    FLINCHED = auto()
    CHARGING = auto()
    RE_CHARGING = auto()

## list of the first round I kind of want to implement
'''
    CURSED = auto()
    SALT_CURED = auto()
    DROWSY = auto()
    BADLY_POISONED = auto()
    IN_LOVE = auto() # "attract"
    ENCORED = auto()
    BOUND = auto()  # "wrap" or "fire spin", etc.
    PERISH_SONG = auto()
    EMBARGOED = auto()
    TAUNTED = auto()
    TORMENTED = auto()
    HEAL_BLOCKED = auto()
    IDENTIFIED = auto()  # by moves like "foresight"
    LEECH_SEED = auto()
    NIGHTMARE = auto()
    CURSED_BODY = auto()
    MAGNETIC_FLUX = auto()  # affected by "magnet rise"
    TELEKINESIS = auto()
    AQUA_RING = auto()
    CENTER_OF_ATTENTION = auto()  # from moves like "follow me", "rage powder"
    RAGE = auto()
    GROUNDED = auto()  # for "gravity"
    TRAPPED = auto()  # "arena trap"
    ROOTED = auto()  # from "ingrain"
    MINIMIZED = auto()
    LASER_FOCUS = auto()
'''
