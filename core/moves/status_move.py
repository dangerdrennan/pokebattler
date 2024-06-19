from interfaces.IMove import MoveInterface
from core.enums.move_category import MoveCategory
from core.enums.pokemon_type import PokemonType

class StatusMove(MoveInterface):
    
    def apply_move(self, attacker, targets, field, history):
        pass

    def get_move_name(self):
        pass

    def get_move_type(self):
        pass

    def get_move_category(self):
        return MoveCategory.STATUS

    def get_pp(self):
        pass

    def get_accuracy(self):
        pass

    pass