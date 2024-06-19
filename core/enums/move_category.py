# core/enums/move_category.py

from enum import Enum, auto

class MoveCategory(Enum):
    PHYSICAL = auto()
    SPECIAL = auto()
    STATUS = auto()
    