# moves/DamageMove.py

from random import randint, randrange, uniform
from interfaces.IMove import MoveInterface
from typing import List
from entities.pokemon import Pokemon
from core.type import Type
from core.enums.pokemon_type import PokemonType, TYPE_DEFENSIVE_MULTIPLIERS, TYPE_OFFENSIVE_MULTIPLIERS
from core.enums.move_category import MoveCategory
from pokebattler.core.enums.secondary_effect_type import SecondaryEffectType
from core.enums.stat import Stat
from core.enums.status.nonvolatile_status import NonVolatileStatus


class DamageMove(MoveInterface):
    '''
    Class for a damage move
    '''
    def __init__(
        self, 
        name: str, 
        move_type: PokemonType, 
        base_power: int, 
        move_category: MoveCategory, 
        priority: int, 
        secondary_effect: SecondaryEffectType,
        accuracy: int = 100,
        secondary_effect_accuracy: int = 100
    ) -> None:
        self.name = name # e.g. Flamethrower
        self.move_category = move_category # Physical or Special
        self.move_type = move_type # e.g. Fire
        self.base_power = base_power # base power of move
        self.priority: int = priority # an int from 1-100
        self.accuracy: int = accuracy # an int from 1-100
        self.secondary_effect_accuracy: int = 100,  
        self.secondary_effect_type = secondary_effect
    
    def get_name(self) -> str:
        return self.name
    
    def get_move_type(self) -> PokemonType:
        return self.move_type
    
    def get_move_category(self):
        pass  # Physical, Special, or Status
    
    def get_pp(self):
        pass
    
    def get_primary_accuracy(self):
        pass
    
    def get_secondary_accuracy(self):
        pass
    
    def get_priority(self):
        pass
    
    def get_status_effect(self):
        pass
    
    def get_secondary_effect(self):
        pass
    
    def get_modified_accuracy(self):
        pass
        
    # stubbed out until I consider this more
    def apply_secondary_effect(self, attacker: Pokemon, target: Pokemon, field = None):
        pass
        
    def apply_move(self, attacker: Pokemon, targets: List[Pokemon]) -> None:
        is_spread = len(targets) > 1
        results_list, secondary_effect_result_list = self.check_success(attacker, targets)
        for i in range(results_list):
            if results_list[i]:
                damage = self.calculate_damage(attacker, targets[i], is_spread)
                targets[i].current_hp = max(0, targets[i].current_hp - damage)
                ## set status to fainted
                if targets[i].current_hp <= 0:
                    targets[i].non_volatile_status = NonVolatileStatus.FAINTED
                ## apply secondary effect if necessary
                else:
                    if secondary_effect_result_list[i]:
                        self.apply_secondary_effect(attacker, targets[i])
        return attacker, targets
    
    def get_relevant_attack_stat(self):
        return Stat.ATTACK if self.move_category == MoveCategory.PHYSICAL else Stat.SPECIAL_ATTACK

    def get_relevant_defense_stat(self):
        return Stat.DEFENSE if self.move_category == MoveCategory.PHYSICAL else Stat.SPECIAL_DEFENSE
    
    def get_stab(self, attacker: Pokemon):
        if self.move_type in (attacker.primary_type, attacker.secondary_type):
            return 1.5
        return 1
    
    def get_initial_damage(self, attacker: Pokemon, attacker_effective_attack, target_effective_defense):
        return (2 * attacker.level / 5 + 2) * self.base_power * (attacker_effective_attack/target_effective_defense) / 50 + 2
        
    def get_typing_modifier(self, target: Pokemon):
        typing_modifier = (TYPE_OFFENSIVE_MULTIPLIERS[self.move_type][target.primary_type.name])
        typing_modifier *= (TYPE_OFFENSIVE_MULTIPLIERS[self.move_type][target.secondary_type.name])
        return typing_modifier
    
    ## I'm writing this with an extra argument, because I know some moves will need to know
    ## a target status
    def get_status_effect_modifier(self, attacker: Pokemon, target: Pokemon):
        if attacker.non_volatile_status == NonVolatileStatus.BURNED and self.move_category == MoveCategory.PHYSICAL:
            return 0.5
        else:
            return 1
    
    def calculate_damage(self, attacker:Pokemon, target:Pokemon, is_spread = False):
        relevant_attack_stat = self.get_relevant_attack_stat()
        relevant_defense_stat = self.get_relevant_defense_stat()
        ## it's simpler to calculate critical hit in the beginning
        is_crit = uniform(0.0, 1.0) < attacker.multipliers.get_multiplier_value(Stat.CRIT_CHANCE)
        # if this is a crit, you need to ignore defense buffs of target and attack debuffs of attacker
        if is_crit:
            target_effective_defense = 1.5 * min(target.get_effective_stat(relevant_defense_stat), target.effective_stats[relevant_defense_stat])
            attacker_effective_attack = 1.5 * max(attacker.get_effective_stat(relevant_attack_stat), attacker.effective_stats[relevant_attack_stat])
        else:
            attacker_effective_attack = attacker.get_effective_stat(relevant_attack_stat)
            target_effective_defense = target.get_effective_stat(relevant_defense_stat)
        ## general formula
        damage = self.get_initial_damage(attacker, attacker_effective_attack, target_effective_defense)
        ## apply STAB
        damage *= self.get_stab(attacker)
        ## apply super effective or resisted modifier
        damage *= self.get_typing_modifier(target)
        ## apply random factor
        damage *= uniform(0.85, 1.0)
        ## halve physcial damage if burned
        damage *= self.get_status_effect_modifier(attacker, target)
        ## apply spread
        if is_spread:
            damage *= 0.75
    
        return damage

    ## todo: apply abilities and held items
    def check_success(self, attacker: Pokemon, targets: List[Pokemon]):
        attacker_accuracy = self.get_modified_accuracy(attacker)
        result_list = [] # list of bools, true if hit, false if miss
        secondary_effect_result_list = [] # list of bools, true if hit, false if miss
        evasiveness_multiplier_list = [self.get_modified_evasion(target) for target in targets]
        for i in range(evasiveness_multiplier_list):
            if randint(1, 100) <= self.accuracy * attacker_accuracy / evasiveness_multiplier_list[i]:
                result_list.append(True)
                if uniform(0, 1) <= self.secondary_effect_accuracy:
                    secondary_effect_result_list.append(False)
            else:
                result_list.append(False)
                secondary_effect_result_list.append(False)
        return result_list, secondary_effect_result_list
        
    # getting modified accuracy depends on a lot of things so I'm seperating this into a helper
    # function for the time being. Helper function is better for expanding in the future
    def get_modified_accuracy(attacker: Pokemon):
        return attacker.multipliers.accuracy.get_multiplier_value()
    
    def get_modified_evasion(target: Pokemon):
        return target.multipliers.evasion.get_multiplier_value()