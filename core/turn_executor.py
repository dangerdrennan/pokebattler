import random

from entities.field import Field
from entities.pokemon import Pokemon
from core.enums.stat import Stat
from core.enums.status.nonvolatile_status import NonVolatileStatus

class TurnExecutor:
    
    def __init__(
        self,
        field: Field,
        attacker: Pokemon,
        participants: list[Pokemon],
    ) -> None:
    
        self.field = field
        self.attacker = attacker
        self.participants = participants
    
    def execute(self):
        self.participants = self.set_turn_order()
        for participant in self.participants:
            # targets = 
            participant.current_move.apply_move(attacker=participant, targets=participant.targets)
            self.participants = [participant for participant in self.participants if participant.non_volatile_status != NonVolatileStatus.FAINTED]
        