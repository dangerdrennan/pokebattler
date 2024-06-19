# core/multipliers.py

from core.enums.stat import Stat
from core.stat_multipliers.standard_stat_stage import StandardStatStage
from core.stat_multipliers.accuracy_stat_stage import AccuracyStatStage
from core.stat_multipliers.evasion_stat_stage import EvasionStatStage
from core.stat_multipliers.crit_stat_stage import CritStatStage

class Multipliers:
    
    def __init__(self):
        
        self.attack = StandardStatStage("Attack")
        self.defense = StandardStatStage("Defense")
        self.sp_attack = StandardStatStage("Special Attack")
        self.sp_defense = StandardStatStage("Special Defense")
        self.speed = StandardStatStage("Speed")
        self.accuracy = AccuracyStatStage("Accuracy")
        self.evasion = EvasionStatStage("Evasion")
        self.critical_hit_multiplier = CritStatStage("Critical Hit Probability")
    
    def get_multiplier_value(self, stat: Stat):
        if stat == Stat.ATTACK:
            return self.attack.get_multiplier_value()
        if stat == Stat.DEFENSE:
            return self.defense.get_multiplier_value()
        if stat == Stat.SPECIAL_ATTACK:
            return self.sp_attack.get_multiplier_value()
        if stat == Stat.SPECIAL_DEFENSE:
            return self.sp_defense.get_multiplier_value()
        if stat == Stat.ACCURACY:
            return self.accuracy.get_multiplier_value()
        if stat == Stat.EVASION:
            return self.evasion.get_multiplier_value()
        if stat == Stat.CRIT_CHANCE:
            return self.critical_hit_multiplier.get_multiplier_value()

    def get_multiplier(self, stat: Stat):
        if stat == Stat.ATTACK:
            return self.attack
        if stat == Stat.DEFENSE:
            return self.defense
        if stat == Stat.SPECIAL_ATTACK:
            return self.sp_attack
        if stat == Stat.SPECIAL_DEFENSE:
            return self.sp_defense
        if stat == Stat.ACCURACY:
            return self.accuracy
        if stat == Stat.EVASION:
            return self.evasion
        if stat == Stat.CRIT_CHANCE:
            return self.critical_hit_multiplier
