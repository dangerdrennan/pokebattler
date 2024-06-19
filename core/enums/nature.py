# core/enums/nature.py

from enum import Enum, auto
from .stat import Stat

class Nature(Enum):
    HARDY = auto()
    LONELY = auto()
    BRAVE = auto()
    ADAMANT = auto()
    NAUGHTY = auto()
    BOLD = auto()
    DOCILE = auto()
    RELAXED = auto()
    IMPISH = auto()
    LAX = auto()
    TIMID = auto()
    HASTY = auto()
    SERIOUS = auto()
    JOLLY = auto()
    NAIVE = auto()
    MODEST = auto()
    MILD = auto()
    QUIET = auto()
    BASHFUL = auto()
    RASH = auto()
    CALM = auto()
    GENTLE = auto()
    SASSY = auto()
    CAREFUL = auto()
    QUIRKY = auto()

nature_effects = {
    Nature.HARDY: (None, None),
    Nature.LONELY: (Stat.ATTACK, Stat.DEFENSE),
    Nature.BRAVE: (Stat.ATTACK, Stat.SPEED),
    Nature.ADAMANT: (Stat.ATTACK, Stat.SPECIAL_ATTACK),
    Nature.NAUGHTY: (Stat.ATTACK, Stat.SPECIAL_DEFENSE),
    Nature.BOLD: (Stat.DEFENSE, Stat.ATTACK),
    Nature.DOCILE: (None, None),
    Nature.RELAXED: (Stat.DEFENSE, Stat.SPEED),
    Nature.IMPISH: (Stat.DEFENSE, Stat.SPECIAL_ATTACK),
    Nature.LAX: (Stat.DEFENSE, Stat.SPECIAL_DEFENSE),
    Nature.TIMID: (Stat.SPEED, Stat.ATTACK),
    Nature.HASTY: (Stat.SPEED, Stat.DEFENSE),
    Nature.SERIOUS: (None, None),
    Nature.JOLLY: (Stat.SPEED, Stat.SPECIAL_ATTACK),
    Nature.NAIVE: (Stat.SPEED, Stat.SPECIAL_DEFENSE),
    Nature.MODEST: (Stat.SPECIAL_ATTACK, Stat.ATTACK),
    Nature.MILD: (Stat.SPECIAL_ATTACK, Stat.DEFENSE),
    Nature.QUIET: (Stat.SPECIAL_ATTACK, Stat.SPEED),
    Nature.BASHFUL: (None, None),
    Nature.RASH: (Stat.SPECIAL_ATTACK, Stat.SPECIAL_DEFENSE),
    Nature.CALM: (Stat.SPECIAL_DEFENSE, Stat.ATTACK),
    Nature.GENTLE: (Stat.SPECIAL_DEFENSE, Stat.DEFENSE),
    Nature.SASSY: (Stat.SPECIAL_DEFENSE, Stat.SPEED),
    Nature.CAREFUL: (Stat.SPECIAL_DEFENSE, Stat.SPECIAL_ATTACK),
    Nature.QUIRKY: (None, None),
}