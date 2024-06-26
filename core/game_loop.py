import random

from utils.input import get_input
from entities.field import Field
from entities.team import Team
from entities.pokemon import Pokemon
from core.enums.stat import Stat
from core.enums.status.nonvolatile_status import NonVolatileStatus

class GameLoop:
    
    def __init__(
        self,
        field: Field,
        participants: list[Pokemon],
        teams: list[Team]
    ) -> None:
    
        self.field = field
        self.participants = participants
        self.opp_left, self.opp_right, self.user_left, self.user_right = participants
        self.teams = teams
        self.turn_order = None
    
    def swap(self, poke_in: Pokemon, poke_out:Pokemon):
        poke_out, poke_in = poke_in, poke_out
        
    def show_board(self):
        max_chars = max((len(self.opp_left.name) + len(self.opp_right.name)), (len(self.user_left.name) + len(self.user_right.name)))
        max_chars += 2
        print(f"{self.opp_left.name}{['x' for x in range(max_chars - len(self.opp_left.name) - len(self.opp_right.name))]}{self.opp_right.name}")
        for i in range(4):
            print(['x' for x in range(max_chars)])
        print(f"{self.user_left.name}{['x' for x in range(max_chars - len(self.user_left.name) - len(self.user_right.name))]}{self.user_right.name}")
        
    def set_turn_order(self) -> list[Pokemon]:
        random.shuffle(self.participants)
        return sorted(self.participants, key=lambda p: (-p.current_move.get_priority(), -p.get_effective_stat(Stat.SPEED)))
    
    def get_user_choice(self, pokemon: Pokemon, team: Team):
        print(f"What will {pokemon.name} do?")
        options = ["1 Withdraw", "2 Attack"]
        choice = get_input(options)
        if choice == '1':
            self.handle_bench(team)
        elif choice == '2':
            self.get_move_choice(pokemon)
    
    def get_move_choice(self, pokemon:Pokemon):
        available_moves = {index: move.name for index, move in enumerate(pokemon.moveset) if move.pp > 0}
        print("Enter the index of the move you want to pick.")
        
    def handle_bench(self, team: Team):
        available_pokemon = {index: pkmn.name for index, pkmn in enumerate(team.pokemon_list) if pkmn not in (self.user_left, self.user_right) and pkmn.non_volatile_status != NonVolatileStatus.FAINTED}
        
        if not available_pokemon:
            print("No pokemon available to switch!")
            return None
        
        print("Choose a pokemon to switch to:")
        for index, name in available_pokemon.items():
            print(f"{index + 1}: {name}")
        
        choice = input("Enter the index of the pokemon: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(available_pokemon):
                selected_pokemon = list(available_pokemon.values())[choice - 1]
                print(f"You chose {selected_pokemon}!")
                return selected_pokemon
            else:
                print("Invalid choice.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None

    def swap(self, poke_in: Pokemon, poke_out: Pokemon):
        if poke_out == self.user_left:
            self.user_left = poke_in
        elif poke_out == self.user_right:
            self.user_right = poke_in
        elif poke_out == self.opp_left:
            self.opp_left = poke_in
        elif poke_out == self.opp_right:
            self.opp_right = poke_in
        
        for i, p in enumerate(self.participants):
            if p == poke_out:
                self.participants[i] = poke_in
                break