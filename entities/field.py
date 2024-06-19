# entities/field.py

from core.enums.weather import Weather
from core.enums.terrain import Terrain
from entities.team import Team
from entities.pokemon import Pokemon


class Field:
    
    def __init__(self, team1: Team, team2: Team):
        
        self.weather = Weather.CLEAR_SKIES
        self.terrain = Terrain.NO_TERRAIN
        self.team1, self.team2 = team1, team2
        self.positions = {
            team1.name: [None, None],
            team2.name: [None, None]
        }
    
    def withdraw(self, team: Team, pokemon_sent_out: Pokemon, pokemon_recalled: Pokemon):
        team_positions = self.positions[team.name]
        
        try:
            index = team_positions.index(pokemon_recalled)
            team_positions[index] = pokemon_sent_out
        except ValueError:
            raise ValueError(f"Pokemon {pokemon_recalled} is not on the field for team {team.name}")
