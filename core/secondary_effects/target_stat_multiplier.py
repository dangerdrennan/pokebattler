# core/secondary_effects/target_stat_multiplier.py

from interfaces.ISecondaryEffect import SecondaryEffectInterface
from entities.pokemon import Pokemon
from core.enums.stat import Stat

class TargetStatMultiplier(SecondaryEffectInterface):

    def __init__(self, stages: int, target_stat: Stat):
        self.stages = stages
        self.target_stat = target_stat

    def apply(self, targets: list[Pokemon], stat: Stat):
        for target in targets:
            target.multipliers.get_multiplier(stat).apply_stage_increments(self.stages)