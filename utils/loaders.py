# utils/loaders.py

import json
from core.type import Type
from core.enums.pokemon_type import PokemonType
from core.enums.moves import Move
from core.base_stats import BaseStats
from core.evs import EVs
from core.ivs import IVs
from core.enums.nature import Nature
from entities.pokemon import Pokemon

def load_pokemon_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    pokemon_list = []
    for item in data:
        base_stats = BaseStats(
            hp=item['base_stats']['stats']['HP'],
            attack=item['base_stats']['stats']['ATTACK'],
            defense=item['base_stats']['stats']['DEFENSE'],
            sp_attack=item['base_stats']['stats']['SPECIAL_ATTACK'],
            sp_defense=item['base_stats']['stats']['SPECIAL_DEFENSE'],
            speed=item['base_stats']['stats']['SPEED']
        )
        
        ivs = IVs(
            hp=item['ivs']['stats']['HP'],
            attack=item['ivs']['stats']['ATTACK'],
            defense=item['ivs']['stats']['DEFENSE'],
            sp_attack=item['ivs']['stats']['SPECIAL_ATTACK'],
            sp_defense=item['ivs']['stats']['SPECIAL_DEFENSE'],
            speed=item['ivs']['stats']['SPEED']
        )
        
        evs = EVs(
            hp=item['evs']['stats']['HP'],
            attack=item['evs']['stats']['ATTACK'],
            defense=item['evs']['stats']['DEFENSE'],
            sp_attack=item['evs']['stats']['SPECIAL_ATTACK'],
            sp_defense=item['evs']['stats']['SPECIAL_DEFENSE'],
            speed=item['evs']['stats']['SPEED']
        )
        
        primary_type = Type(getattr(PokemonType, item['primary_type'].split('.')[1]))
        secondary_type = Type(getattr(PokemonType, item['secondary_type'].split('.')[1])) if item['secondary_type'] else None
        nature = getattr(Nature, item['nature'].split('.')[1])
        moveset =  [Move[move].get_copy() for move in item['moveset']] if item['moveset'] else []
        
        pokemon = Pokemon(
            name=item['name'],
            gender=item['gender'],
            ability=item['ability'],
            moveset=moveset,
            base_stats=base_stats,
            ivs=ivs,
            evs=evs,
            primary_type=primary_type,
            secondary_type=secondary_type,
            can_evolve=item['can_evolve'],
            held_item=item['held_item'],
            nature=nature,
            level=item['level'],
        )
        
        pokemon_list.append(pokemon)
        
    return pokemon_list
