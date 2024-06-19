# interfaces/SecondaryEffectInterface.py

from abc import ABC, abstractmethod
from entities.pokemon import Pokemon

class SecondaryEffectInterface(ABC):

    @abstractmethod
    def apply(self, attacker: Pokemon, targets = None, field = None):
        pass

    