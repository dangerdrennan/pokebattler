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
        self.turn_order = None
    
    def execute(self):
        
        self.participants = self.set_turn_order()
        for participant in self.participants:
            participant.current_move.apply_move(attacker=participant, targets=participant.targets)
            self.participants = [participant for participant in self.participants if participant.non_volatile_status != NonVolatileStatus.FAINTED]
        
    def set_turn_order(self) -> list[Pokemon]:
        random.shuffle(self.participants)
        return sorted(self.participants, key=lambda p: (-p.current_move.get_priority(), -p.get_effective_stat(Stat.SPEED)))
    