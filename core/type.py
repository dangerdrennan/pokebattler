# core/type.py

from core.enums.pokemon_type import PokemonType
    
class Type:
    def __init__(self, name: PokemonType):
        self.name = name
        
    
    def __str__(self):
        return self.name.name.capitalize()