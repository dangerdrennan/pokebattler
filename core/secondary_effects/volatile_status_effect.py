# core/secondary_effects/nonvolatile_status_effect.py

from random import randint
from interfaces.ISecondaryEffect import SecondaryEffectInterface
from entities.pokemon import Pokemon
from core.enums.status.volatile_status import VolatileStatus

class VolatileStatusEffect(SecondaryEffectInterface):

    def __init__(self, status_effect: VolatileStatus, accuracy: int = 100, num_turns = float('inf')):
        self.status_effect = status_effect
        self.accuracy = accuracy
        self.num_turns = num_turns
    
    def apply(self, targets: list[Pokemon]):
        for target in targets:
            if randint(1,100) <= self.accuracy:
                if self.status_effect not in target.volatile_status.keys():
                    target.volatile_status[self.status_effect] = self.num_turns
    
    