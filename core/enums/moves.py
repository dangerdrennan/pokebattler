# data/moves.py

from enum import Enum
from core.moves.damage_move import DamageMove
from core.secondary_effects.nonvolatile_status_effect import NonVolatileStatusAffliction
from core.enums.move_category import MoveCategory
from core.enums.status.nonvolatile_status import NonVolatileStatus
from core.enums.pokemon_type import PokemonType

class Move(Enum):
    EXTREME_SPEED = DamageMove(name='Extreme Speed', move_type=PokemonType.NORMAL, base_power=80, move_category=MoveCategory.PHYSICAL, priority=2, secondary_effect=None, accuracy=100, pp=5)
    SACRED_FIRE = DamageMove(name='Sacred Fire', move_type=PokemonType.FIRE, base_power=100, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.BURNED, accuracy=50), accuracy=95, pp=5)
    ICE_BEAM = DamageMove(name='Ice Beam', move_type=PokemonType.ICE, base_power=90, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.FROZEN, accuracy=10), accuracy=100, pp=10)
    BLIZZARD = DamageMove(name='Blizzard', move_type=PokemonType.ICE, base_power=110, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.FROZEN, accuracy=10), accuracy=70, pp=5)
    PROTECT = DamageMove(name='Protect', move_type=PokemonType.NORMAL, base_power=0, move_category=MoveCategory.STATUS, priority=4, secondary_effect=None, accuracy=float('inf'), pp=10)
    
    def get_copy(self):
        return self.value.copy()