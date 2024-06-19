from utils.loaders import load_pokemon_data
from entities.team import Team

def main():
    pokemon_data_file = 'fixtures/pokemon.json'
    pokemon_list = load_pokemon_data(pokemon_data_file)
    
    # Split Pokémon into two teams
    legendary_birds = Team(pokemon_list[:3], name="Legendary Birds")
    legendary_dogs = Team(pokemon_list[3:6], name="Legendary Dogs")
    
    # Print team details
    print(f"Team {legendary_birds.name}: {[pokemon.name for pokemon in legendary_birds.pokemon_list]}")
    print(f"Team {legendary_dogs.name}: {[pokemon.name for pokemon in legendary_dogs.pokemon_list]}")

if __name__ == '__main__':
    main()
