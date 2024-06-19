# entities/team.py

from entities.pokemon import Pokemon

class Team:
    def __init__(self, pokemon_list: list[Pokemon], name: str = None):
        self.pokemon_list = pokemon_list
        ## the dictionary is string names -> bool
        self.available_pokemon: dict[str, bool] = {pokemon.name: True for pokemon in pokemon_list}
        self.name = name if name else f'Team {", ".join([pokemon.name for pokemon in pokemon_list[:-1]])}, and {pokemon_list[-1].name}'
        
    
    ## updates the list of pokemon with remaining hp
    ## I believe this will be for display reasons only, not 100% sure yet
    def update_available(self):
        self.available_pokemon = {pokemon.name: True for pokemon in self.pokemon_list if pokemon.current_hp >= 0}
    
    def set_new_order(self, ordered_list):
        self.pokemon_list = ordered_list