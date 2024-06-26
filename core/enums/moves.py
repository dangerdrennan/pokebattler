# data/moves.py

from enum import Enum
from core.moves.damage_move import DamageMove
from core.secondary_effects.nonvolatile_status_effect import NonVolatileStatusAffliction
from core.secondary_effects.volatile_status_effect import VolatileStatusEffect
from core.enums.move_category import MoveCategory
from core.enums.status.nonvolatile_status import NonVolatileStatus
from core.enums.status.volatile_status import VolatileStatus
from core.enums.pokemon_type import PokemonType

class Move(Enum):
    EXTREME_SPEED = DamageMove(name='Extreme Speed', move_type=PokemonType.NORMAL, base_power=80, move_category=MoveCategory.PHYSICAL, priority=2, secondary_effect=None, accuracy=100, pp=5)
    SACRED_FIRE = DamageMove(name='Sacred Fire', move_type=PokemonType.FIRE, base_power=100, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.BURNED, accuracy=50), accuracy=95, pp=5)
    ICE_BEAM = DamageMove(name='Ice Beam', move_type=PokemonType.ICE, base_power=90, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.FROZEN, accuracy=10), accuracy=100, pp=10)
    BLIZZARD = DamageMove(name='Blizzard', move_type=PokemonType.ICE, base_power=110, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.FROZEN, accuracy=10), accuracy=70, pp=5)
    PROTECT = DamageMove(name='Protect', move_type=PokemonType.NORMAL, base_power=0, move_category=MoveCategory.STATUS, priority=4, secondary_effect=None, accuracy=float('inf'), pp=10)
    SHEER_COLD = DamageMove(name='Sheer Cold', move_type=PokemonType.ICE, base_power=0, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=None, accuracy=30, pp=5)
    HYDRO_PUMP = DamageMove(name='Hydro Pump', move_type=PokemonType.WATER, base_power=110, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=None, accuracy=80, pp=5)
    HURRICANE = DamageMove(name='Hurricane', move_type=PokemonType.FLYING, base_power=110, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=VolatileStatusEffect(VolatileStatus.CONFUSED, accuracy=30), accuracy=70, pp=10)
    THUNDER = DamageMove(name='Thunder', move_type=PokemonType.ELECTRIC, base_power=110, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.PARALYZED, accuracy=30), accuracy=70, pp=10)
    HEAT_WAVE = DamageMove(name='Heat Wave', move_type=PokemonType.FIRE, base_power=95, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.BURNED, accuracy=10), accuracy=90, pp=10)
    IRON_HEAD = DamageMove(name='Iron Head', move_type=PokemonType.STEEL, base_power=80, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=VolatileStatusEffect(VolatileStatus.FLINCHED, accuracy=30), accuracy=100, pp=15)
    AIR_SLASH = DamageMove(name='Air Slash', move_type=PokemonType.FLYING, base_power=75, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=VolatileStatusEffect(VolatileStatus.FLINCHED, accuracy=30), accuracy=95, pp=15)
    DISCHARGE = DamageMove(name='Discharge', move_type=PokemonType.ELECTRIC, base_power=80, move_category=MoveCategory.SPECIAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.PARALYZED, accuracy=30), accuracy=100, pp=15)
    ## TO DO:
    # FLARE_BLITZ = DamageMove(name='Flare Blitz', move_type=PokemonType.FIRE, base_power=120, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.BURNED, accuracy=10), accuracy=100, pp=15, recoil=33)
    # PROTECT = StatusMove(name='Protect', move_type=PokemonType.NORMAL, base_power=0, move_category=MoveCategory.STATUS, priority=4, secondary_effect=None, accuracy=float('inf'), pp=10)
    # SKY_ATTACK = DamageMove(name='Sky Attack', move_type=PokemonType.FLYING, base_power=140, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=VolatileStatusEffect(VolatileStatus.FLINCHED, accuracy=30), accuracy=90, pp=5, charge_turns=1)
    # GIGA_IMPACT = DamageMove(name='Giga Impact', move_type=PokemonType.NORMAL, base_power=150, move_category=MoveCategory.PHYSICAL, priority=0, secondary_effect=None, accuracy=90, pp=5, recharge_turns=1)
    # RAIN_DANCE = StatusMove(name='Rain Dance', move_type=PokemonType.WATER, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=None, accuracy=float('inf'), pp=5, weather='rain')
    # TAILWIND = StatusMove(name='Tailwind', move_type=PokemonType.FLYING, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=StatChangeEffect(stat='speed', stages=2, target='ally'), accuracy=float('inf'), pp=15)
    # THUNDER_WAVE = StatusMove(name='Thunder Wave', move_type=PokemonType.ELECTRIC, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.PARALYZED, accuracy=100), accuracy=90, pp=20)
    # AGILITY = StatusMove(name='Agility', move_type=PokemonType.PSYCHIC, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=StatChangeEffect(stat='speed', stages=2, target='self'), accuracy=float('inf'), pp=30)
    # ROOST = StatusMove(name='Roost', move_type=PokemonType.FLYING, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=StatChangeEffect(stat='hp', stages=0, target='self'), accuracy=float('inf'), pp=10, heal=50)
    # LIGHT_SCREEN = StatusMove(name='Light Screen', move_type=PokemonType.PSYCHIC, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=StatChangeEffect(stat='special_defense', stages=2, target='ally'), accuracy=float('inf'), pp=30)
    # REST = StatusMove(name='Rest', move_type=PokemonType.PSYCHIC, base_power=0, move_category=MoveCategory.STATUS, priority=0, secondary_effect=NonVolatileStatusAffliction(NonVolatileStatus.SLEEP, accuracy=float('inf')), accuracy=float('inf'), pp=10, heal=100)
    
    def get_copy(self):
        return self.value.copy()