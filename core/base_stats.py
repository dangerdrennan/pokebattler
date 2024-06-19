# core/base_stats.py

from core.enums.stat import Stat
from core.enums.nature import Nature, nature_effects

class BaseStats:
  
    def __init__(self, hp: int = 0, attack: int = 0, defense: int = 0, sp_attack: int = 0, sp_defense: int = 0, speed: int = 0, nature: Nature = None):
        self.stats = {
            Stat.HP: hp,
            Stat.ATTACK: attack,
            Stat.DEFENSE: defense,
            Stat.SPECIAL_ATTACK: sp_attack,
            Stat.SPECIAL_DEFENSE: sp_defense,
            Stat.SPEED: speed
        }
        self.nature = nature

    def calculate_hp(self, iv: int = 0, ev: int = 0, level: int = 50) -> int:
        return ((2 * self.stats[Stat.HP] + iv + (ev // 4)) * level) // 100 + level + 10

    def calculate_stat(self, stat: Stat, iv: int = 0, ev: int = 0, level: int = 50, nature: Nature = None) -> int:
        initial_base_stat = self.stats[stat]
        new_stat = ((2 * initial_base_stat + iv + (ev // 4)) * level) // 100 + 5
        
        if nature:
            increase, decrease = nature_effects[nature]
            if stat == increase: return new_stat * 1.1
            elif stat == decrease: return new_stat * 0.9
        
        return new_stat   
