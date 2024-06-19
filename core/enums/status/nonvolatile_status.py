# core/enums/nonvolatile_status.py

from enum import Enum, auto

class NonVolatileStatus(Enum):
    BURNED = auto()
    FROZEN = auto()
    PARALYZED = auto()
    POISONED = auto()
    SLEEPING = auto()
    HEALTHY = auto()
    FAINTED = auto()

'''
the next list of Statuses I'm thinking of adding
    CONFUSED = auto()
    CURSED = auto()
    SALT_CURED = auto()
    DROWSY = auto()
    BADLY_POISONED = auto()
    IN_LOVE = auto() # "attract"
    ENCORED = auto()
    BOUND = auto()  # "wrap" or "fire spin", etc.
    PERISH_SONG = auto()
    EMBARGOED = auto()
    TAUNTED = auto()
    TORMENTED = auto()
    HEAL_BLOCKED = auto()
    IDENTIFIED = auto()  # by moves like "foresight"
    LEECH_SEED = auto()
    NIGHTMARE = auto()
    CURSED_BODY = auto()
    MAGNETIC_FLUX = auto()  # affected by "magnet rise"
    TELEKINESIS = auto()
    AQUA_RING = auto()
    CENTER_OF_ATTENTION = auto()  # from moves like "follow me", "rage powder"
    RAGE = auto()
    GROUNDED = auto()  # for "gravity"
    TRAPPED = auto()  # "arena trap"
    ROOTED = auto()  # from "ingrain"
    MINIMIZED = auto()
    LASER_FOCUS = auto()
from bulbapedia:
1.1	Non-volatile status
1.1.1	Burn
1.1.2	Freeze
1.1.2.1	Frostbite
1.1.3	Paralysis
1.1.4	Poison
1.1.4.1	Badly poisoned
1.1.5	Sleep
1.1.5.1	Drowsy
1.2	Volatile status
1.2.1	Major
1.2.1.1	Ability change
1.2.1.2	Ability suppression
1.2.1.3	Type change
1.2.1.4	Mimic
1.2.1.5	Substitute
1.2.1.6	Transformed
1.2.1.7	Illusion
1.2.2	Damaging
1.2.2.1	Bound
1.2.2.2	Curse
1.2.2.3	Nightmare
1.2.2.4	Perish Song
1.2.2.5	Seeded
1.2.2.6	Salt Cure
1.2.2.7	Splinters
1.2.3	Effectiveness
1.2.3.1	Autotomize
1.2.3.2	Identified
1.2.3.3	Minimize
1.2.3.4	Tar Shot
1.2.4	Groundedness
1.2.4.1	Grounded
1.2.4.2	Magnetic levitation
1.2.4.3	Telekinesis
1.2.5	Healing
1.2.5.1	Aqua Ring
1.2.5.2	Rooting
1.2.6	Next Turn
1.2.6.1	Laser Focus
1.2.6.2	Taking aim
1.2.6.3	Drowsy
1.2.7	Priming
1.2.7.1	Charged
1.2.7.2	Stockpile count
1.2.7.3	Defense Curl
1.2.7.4	Primed
1.2.8	Prevention
1.2.8.1	Can't escape
1.2.8.1.1	No retreat
1.2.8.1.2	Octolock
1.2.8.2	Disable
1.2.8.3	Embargo
1.2.8.4	Heal Block
1.2.8.5	Imprison
1.2.8.6	Taunt
1.2.8.7	Throat Chop
1.2.8.8	Torment
1.2.8.9	Confusion
1.2.8.10	Infatuation
1.2.9	Stats
1.2.9.1	Getting pumped
1.2.9.2	Guard Split
1.2.9.3	Power Split
1.2.9.4	Speed Swap
1.2.9.5	Power Trick
1.2.9.6	Power Boost
1.2.9.7	Power Drop
1.2.9.8	Guard Boost
1.2.9.9	Guard Drop
1.2.9.10	Critical Hit Boost
1.2.9.11	Obscured
1.2.10	Forced Move
1.2.10.1	Choice lock
1.2.10.2	Encore
1.2.10.3	Rampage
1.2.10.4	Rolling
1.2.10.5	Making an uproar
1.2.10.6	Fixated
1.2.11	Multi-turn Move
1.2.11.1	Bide
1.2.11.2	Recharging
1.2.11.3	Charging turn
1.2.11.3.1	Moves
1.2.11.3.2	Semi-invulnerable turn
1.2.12	Transient
1.2.12.1	Flinch
1.2.12.2	Bracing
1.2.12.3	Center of attention
1.2.12.4	Magic Coat
1.2.12.5	Protection
'''