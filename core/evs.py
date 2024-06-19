# core/evs.py

from core.enums.stat import Stat

class EVs:
    def __init__(self, hp: int = 0, attack: int = 0, defense: int = 0, sp_attack: int = 0, sp_defense: int = 0, speed: int = 0):
        if (hp > 252 or attack > 252 or sp_attack > 252 or sp_defense > 252 or speed > 252):
            return Exception("Cannot apply an EV over 252 to any single stat.")
        if (hp < 0 or attack < 0 or sp_attack < 0 or sp_defense < 0 or speed < 0):
            return Exception("EV values cannot be negative.")
        if (sum([hp, attack, sp_attack, sp_defense, speed]) > 510):
            return Exception("Cannot apply a total EV spread of over 510.")
        
        self.values = {
            Stat.HP: hp,
            Stat.ATTACK: attack,
            Stat.DEFENSE: defense,
            Stat.SPECIAL_ATTACK: sp_attack,
            Stat.SPECIAL_DEFENSE: sp_defense,
            Stat.SPEED: speed
        }

    def get_ev(self, stat: Stat) -> int:
        return self.values.get(stat, 0)
    
    def set_ev(self, stat: Stat, num: int) -> None:
        self.values[stat] = num
        
    def __eq__(self, obj) -> bool:
        return self.values == obj.values
    