# core/ivs.py

from core.enums.stat import Stat

class IVs:
    def __init__(self, hp: int = 0, attack: int = 0, defense: int = 0, sp_attack: int = 0, sp_defense: int = 0, speed: int = 0):
        if any(iv > 31 for iv in [hp, attack, defense, sp_attack, sp_defense, speed]):
            raise ValueError("IV values cannot be greater than 31.")
        if any(iv < 0 for iv in [hp, attack, defense, sp_attack, sp_defense, speed]):
            raise ValueError("IV values cannot be negative.")
        
        self.values = {
            Stat.HP: hp,
            Stat.ATTACK: attack,
            Stat.DEFENSE: defense,
            Stat.SPECIAL_ATTACK: sp_attack,
            Stat.SPECIAL_DEFENSE: sp_defense,
            Stat.SPEED: speed
        }

    def get_iv(self, stat: Stat) -> int:
        return self.values.get(stat, 0)
    
    def set_iv(self, stat: Stat, num: int) -> None:
        self.values[stat] = num
        
    def __eq__(self, obj) -> bool:
            return self.values == obj.values
        