# core/enums/pokemon_type.py

from enum import Enum, auto

class PokemonType(Enum):
    FIRE = auto()
    WATER = auto()
    GRASS = auto()
    BUG = auto()
    ROCK = auto()
    STEEL = auto()
    ICE = auto()
    DRAGON = auto()
    GHOST = auto()
    FAIRY = auto()
    NORMAL = auto()
    GROUND = auto()
    FLYING = auto()
    ELECTRIC = auto()
    DARK = auto()
    POISON = auto()
    FIGHTING = auto()
    PSYCHIC = auto()
    TYPELESS = auto()
    
## Only adding enough for the Kanto legendary birds and Johto legendary dogs right now

TYPE_OFFENSIVE_MULTIPLIERS = {
    PokemonType.FLYING : {
        PokemonType.FIRE : 1,
        PokemonType.WATER : 1,
        PokemonType.GRASS : 2,
        PokemonType.BUG : 2,
        PokemonType.ROCK : 0.5,
        PokemonType.STEEL : 0.5,
        PokemonType.ICE : 1,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 1,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC : 0.5,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 2,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.FIRE: {
        PokemonType.FIRE : 1,
        PokemonType.WATER : 0.5,
        PokemonType.GRASS : 2,
        PokemonType.BUG : 2,
        PokemonType.ROCK : 0.5,
        PokemonType.STEEL : 2,
        PokemonType.ICE : 2,
        PokemonType.DRAGON : 0.5,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 1,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC :1,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.ICE: {
        PokemonType.FIRE : 0.5,
        PokemonType.WATER : 0.5,
        PokemonType.GRASS : 2,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 1,
        PokemonType.STEEL : 0.5,
        PokemonType.ICE : 0.5,
        PokemonType.DRAGON : 2,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 2,
        PokemonType.FLYING : 2,
        PokemonType.ELECTRIC : 1,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.ELECTRIC: {
        PokemonType.FIRE : 1,
        PokemonType.WATER : 2,
        PokemonType.GRASS : 0.5,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 1,
        PokemonType.STEEL : 1,
        PokemonType.ICE : 1,
        PokemonType.DRAGON : 0.5,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 0,
        PokemonType.FLYING : 2,
        PokemonType.ELECTRIC : 0.5,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.WATER: {
        PokemonType.FIRE : 2,
        PokemonType.WATER : 0.5,
        PokemonType.GRASS : 0.5,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 2,
        PokemonType.STEEL : 1,
        PokemonType.ICE : 1,
        PokemonType.DRAGON : 0.5,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 2,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC : 1,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
}

TYPE_DEFENSIVE_MULTIPLIERS = {
    PokemonType.FLYING : {
        PokemonType.FIRE : 1,
        PokemonType.WATER : 1,
        PokemonType.GRASS : 0.5,
        PokemonType.BUG : 0.5,
        PokemonType.ROCK : 2,
        PokemonType.STEEL : 1,
        PokemonType.ICE : 2,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 1,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC : 2,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 0.5,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.FIRE: {
        PokemonType.FIRE : 0.5,
        PokemonType.WATER : 2,
        PokemonType.GRASS : 0.5,
        PokemonType.BUG : 0.5,
        PokemonType.ROCK : 2,
        PokemonType.STEEL : 1,
        PokemonType.ICE : 0.5,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 0.5,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 2,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC :1,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.ICE: {
        PokemonType.FIRE : 2,
        PokemonType.WATER : 1,
        PokemonType.GRASS : 1,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 2,
        PokemonType.STEEL : 2,
        PokemonType.ICE : 0.5,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 1,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC : 1,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 2,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.ELECTRIC: {
        PokemonType.FIRE : 1,
        PokemonType.WATER : 1,
        PokemonType.GRASS : 1,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 1,
        PokemonType.STEEL : 0.5,
        PokemonType.ICE : 1,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 2,
        PokemonType.FLYING : 0.5,
        PokemonType.ELECTRIC : 0.5,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
    PokemonType.WATER: {
        PokemonType.FIRE : 0.5,
        PokemonType.WATER : 0.5,
        PokemonType.GRASS : 2,
        PokemonType.BUG : 1,
        PokemonType.ROCK : 1,
        PokemonType.STEEL : 0.5,
        PokemonType.ICE : 1,
        PokemonType.DRAGON : 1,
        PokemonType.GHOST : 1,
        PokemonType.FAIRY : 1,
        PokemonType.NORMAL : 1,
        PokemonType.GROUND : 1,
        PokemonType.FLYING : 1,
        PokemonType.ELECTRIC : 2,
        PokemonType.DARK : 1,
        PokemonType.POISON : 1,
        PokemonType.FIGHTING : 1,
        PokemonType.PSYCHIC : 1,
        PokemonType.TYPELESS : 1
    },
}