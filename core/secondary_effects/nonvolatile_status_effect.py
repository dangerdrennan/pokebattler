# core/secondary_effects/nonvolatile_status_effect.py

from random import randint
from interfaces.ISecondaryEffect import SecondaryEffectInterface
from entities.pokemon import Pokemon
from core.enums.status.nonvolatile_status import NonVolatileStatus

class NonVolatileStatusAffliction(SecondaryEffectInterface):

    def __init__(self, status_affliction: NonVolatileStatus, accuracy: int = 100):
        self.status_affliction = status_affliction
        self.accuracy = accuracy

    ## starting implementation that follows gen 1 mechanics, i.e. Electric types can be 
    ## inflicted with paralysis, Fire types can be burned, etc. Will update later.
    def apply(self, targets: list[Pokemon]):
        for target in targets:
            if randint(1,100) <= self.accuracy:
                if target.non_volatile_status == NonVolatileStatus.HEALTHY:
                    target.non_volatile_status = self.status_affliction