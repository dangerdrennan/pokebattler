from utils.loaders import load_pokemon_data
from utils.input import get_input
from utils.parsers import choose_lead_pokemon
from entities.team import Team
from entities.pokemon import Pokemon

def demo():
    pokemon_data_file = 'pokebattler/fixtures/pokemon.json'
    pokemon_list: list[Pokemon] = load_pokemon_data(pokemon_data_file)
    user_team: Team = None

    for pokemon in pokemon_list:
        print(pokemon.name, pokemon.level)

    print("Welcome to pokemon battler, the only pokemon battle simulator ever attempted. (enter 'q' at any time to quit)")
    print("Please select your team- 1 for the legendary birds of Kanto or 2 for the legendary dogs of Johto.")
    # choice = get_input("")
    choice = '1'
    if choice == '1':
        user_team = Team(pokemon_list[:3], name="Legendary Birds")
        computer_team = Team(pokemon_list[3:], name="Legendary Dogs")
    elif choice == '2':
        user_team = Team(pokemon_list[3:], name="Legendary Dogs")
        computer_team = Team(pokemon_list[:3], name="Legendary Birds")
    else:
        print("Okay, I'm just giving you the Kanto birds to speed this along. Congrats, you'll love them.")
        user_team = Team(pokemon_list[:3], name="Legendary Birds")
        computer_team = Team(pokemon_list[3:], name="Legendary Dogs")

    print("This is a demo of a 3-3 double battle.")
    print("Enter the indexes of the two pokemon you want to lead with and the other you'll have in the back.")
    lead_indices = []
    pokemon_position_dictionary = {}
    for i, pokemon in enumerate(user_team.pokemon_list):
        pokemon_position_dictionary[i + 1] = pokemon.name
        print(f"{i + 1} {pokemon.name}  ")

    # while not lead_indices:
    #     try:
    #         lead_indices = choose_lead_pokemon()
    #     except Exception as e:
    #         print(e)
    #         print("Error occurred in parsing choice. Please try again or press 'q' to exit.")
    lead_indices= [1,2]

    ordered_list = []
    ordered_list.append(pokemon_list[int(lead_indices[0]) - 1])
    ordered_list.append(pokemon_list[int(lead_indices[1]) - 1])
    ordered_list.extend([pokemon for pokemon in pokemon_list if pokemon not in ordered_list])

    user_team.set_new_order(ordered_list)
    
    print(f"Perfect, you're leading with {ordered_list[0].name} and {ordered_list[1].name}")
    print(f"Rival trainer is leading with {computer_team.pokemon_list[0].name} and {computer_team.pokemon_list[1].name}")
    
    cur_poke = user_team.pokemon_list[0]
    other_poke = computer_team.pokemon_list[0]
    chosen_move = user_team.pokemon_list[0].moveset[0]
    
    print(cur_poke.__dict__)
    print(other_poke.__dict__)
    
    chosen_move.apply_move(cur_poke, [other_poke])
    print("worked?")
    print()
    
    print(cur_poke.__dict__)
    print(other_poke.__dict__)
    
    
    
if __name__ == '__main__':
    demo()
