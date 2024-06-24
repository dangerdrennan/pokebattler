# entities/pokemon.py

from core.ability import Ability
from core.base_stats import BaseStats
from core.multipliers import Multipliers
from core.ivs import IVs
from core.evs import EVs
from core.type import Type
from core.enums.stat import Stat
from core.enums.pokemon_type import PokemonType
from core.enums.status.nonvolatile_status import NonVolatileStatus 
from core.enums.status.volatile_status import VolatileStatus ## WIP, unsure if needed anywhere in Pokemon class
from core.enums.nature import Nature
from interfaces.IMove import MoveInterface

class Pokemon:
    
    def __init__(
        self, 
        name: str, 
        gender: str,
        ability: Ability = None,
        moveset = None,
        base_stats: BaseStats = None,
        ivs: IVs = None,
        evs: EVs = None,
        primary_type: Type = None,
        secondary_type: Type = None,
        can_evolve: bool = False,
        held_item = None, # class not implemented yet
        nature: Nature = Nature.QUIRKY,
        level: int = 50,
    ) -> None:
        self.name = name
        self.gender = gender
        self.ability = ability if ability else Ability()
        self.moveset = moveset if moveset else {}
        self.base_stats = base_stats if base_stats else BaseStats()
        self.ivs = ivs if ivs else IVs(31, 31, 31, 31, 31, 31)
        self.evs = evs if evs else EVs(0, 0, 0, 0, 0, 0)
        self.multipliers = Multipliers()
        self.primary_type = primary_type
        self.secondary_type = secondary_type if secondary_type else None
        self.can_evolve = False
        self.held_item = None
        self.nature = None
        self.level = 50
        self.non_volatile_status = NonVolatileStatus.HEALTHY
        self.volatile_status = {}
        self.nature = nature
        self.effective_stats = self.set_effective_stats()
        self.current_hp = self.effective_stats[Stat.HP]
        self.moveset = moveset
        self.current_move: MoveInterface = None
        self.targets = list[Pokemon]
        
    # To do: this is a placeholder for testing and development- replace with better attributes
    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return self.name == other.name 
        return False
        
    def set_effective_stats(self) -> dict[Stat, int]:
        effective_stats = {
            Stat.HP: self.base_stats.calculate_hp(self.ivs.values[Stat.HP], self.evs.values[Stat.HP], self.level),
            Stat.ATTACK: self.base_stats.calculate_stat(Stat.ATTACK, self.ivs.values[Stat.ATTACK], self.evs.values[Stat.ATTACK], self.level),
            Stat.DEFENSE: self.base_stats.calculate_stat(Stat.DEFENSE, self.ivs.values[Stat.DEFENSE], self.evs.values[Stat.DEFENSE], self.level),
            Stat.SPECIAL_ATTACK: self.base_stats.calculate_stat(Stat.SPECIAL_ATTACK, self.ivs.values[Stat.SPECIAL_ATTACK], self.evs.values[Stat.SPECIAL_ATTACK], self.level),
            Stat.SPECIAL_DEFENSE: self.base_stats.calculate_stat(Stat.SPECIAL_DEFENSE, self.ivs.values[Stat.SPECIAL_DEFENSE], self.evs.values[Stat.SPECIAL_DEFENSE], self.level),
            Stat.SPEED: self.base_stats.calculate_stat(Stat.SPEED, self.ivs.values[Stat.SPEED], self.evs.values[Stat.SPEED], self.level)
        }
        return effective_stats
    
    def get_effective_stat(self, stat: Stat) -> int:
        return self.effective_stats[stat] * self.multipliers.get_multiplier_value(stat)
    
    # don't return ability yet, not implemented
    def get_ability(self) -> None:
        pass