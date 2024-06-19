# core/enums/secondary_effect_type.py

from enum import Enum, auto

class SecondaryEffectType(Enum):
    TARGET_STAT_MULTIPLIER = auto()
    SELF_STAT_MULTIPLIER = auto()
    TARGET_NONVOLATILE_CONDITION = auto()
    SELF_NONVOLATILE_CONDITION = auto()
    TARGET_VOLATILE_CONDITION = auto()
    SELF_VOLATILE_CONDITION = auto()