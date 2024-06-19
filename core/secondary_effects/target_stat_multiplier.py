from interfaces.ISecondaryEffect import SecondaryEffectInterface
from entities.pokemon import Pokemon
from enums.stat import Stat

class TargetStatMultiplier(SecondaryEffectInterface):

    def __init__(self, stages: int, target_stat: Stat):
        self.stages = stages
        self.target_stat = target_stat

    def apply(self,
              attacker: Pokemon,
              targets: list[Pokemon],
              field,
              stat: Stat,
              
              ):
        for target in targets:
            if (self.stages < 0):
                target.multipliers.get_multiplier