# tests/test_initialization.py

import unittest
from core.ivs import IVs
from core.evs import EVs
from core.type import Type
from core.base_stats import BaseStats
from entities.pokemon import Pokemon
from core.enums.stat import Stat
from core.enums.nature import Nature
from core.type import PokemonType

class TestInitialization(unittest.TestCase):

    def test_ivs_initialization(self):
        ivs = IVs(hp=31, attack=31, defense=31, sp_attack=31, sp_defense=31, speed=31)
        self.assertEqual(ivs.get_iv(Stat.HP), 31)
        self.assertEqual(ivs.get_iv(Stat.ATTACK), 31)
        self.assertEqual(ivs.get_iv(Stat.DEFENSE), 31)
        self.assertEqual(ivs.get_iv(Stat.SPECIAL_ATTACK), 31)
        self.assertEqual(ivs.get_iv(Stat.SPECIAL_DEFENSE), 31)
        self.assertEqual(ivs.get_iv(Stat.SPEED), 31)

    def test_evs_initialization(self):
        evs = EVs(hp=0, attack=0, defense=0, sp_attack=0, sp_defense=0, speed=0)
        self.assertEqual(evs.values[Stat.HP], 0)
        self.assertEqual(evs.values[Stat.ATTACK], 0)
        self.assertEqual(evs.values[Stat.DEFENSE], 0)
        self.assertEqual(evs.values[Stat.SPECIAL_ATTACK], 0)
        self.assertEqual(evs.values[Stat.SPECIAL_DEFENSE], 0)
        self.assertEqual(evs.values[Stat.SPEED], 0)

    def test_base_stats_initialization(self):
        base_stats = BaseStats(hp=78, attack=84, defense=78, sp_attack=109, sp_defense=85, speed=100)
        self.assertEqual(base_stats.stats[Stat.HP], 78)
        self.assertEqual(base_stats.stats[Stat.ATTACK], 84)
        self.assertEqual(base_stats.stats[Stat.DEFENSE], 78)
        self.assertEqual(base_stats.stats[Stat.SPECIAL_ATTACK], 109)
        self.assertEqual(base_stats.stats[Stat.SPECIAL_DEFENSE], 85)
        self.assertEqual(base_stats.stats[Stat.SPEED], 100)

    def test_pokemon_initialization(self):
        base_stats = BaseStats(hp=78, attack=84, defense=78, sp_attack=109, sp_defense=85, speed=100)
        ivs = IVs(hp=31, attack=31, defense=31, sp_attack=31, sp_defense=31, speed=31)
        evs = EVs(hp=0, attack=0, defense=0, sp_attack=0, sp_defense=0, speed=0)
        charizard = Pokemon(name = "Charizard", 
                            gender = "Male", 
                            base_stats = base_stats, 
                            ivs = ivs, 
                            evs = evs, 
                            primary_type = Type(PokemonType.FIRE), 
                            secondary_type = Type(PokemonType.FLYING),
                            can_evolve = False,
                            nature = Nature.JOLLY)
        self.assertEqual(charizard.name, "Charizard")
        self.assertEqual(charizard.gender, "Male")
        self.assertEqual(charizard.base_stats, base_stats)
        self.assertEqual(charizard.ivs, ivs)
        self.assertEqual(charizard.evs, evs)

if __name__ == '__main__':
    unittest.main()
