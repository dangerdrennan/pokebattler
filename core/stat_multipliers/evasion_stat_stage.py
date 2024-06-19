# stat_multipliers/evasion_stat_stage.py

from interfaces.IMultiplier import StatStageBase

class EvasionStatStage(StatStageBase):
    
    STAGE_MULTIPLIERS = {
        -6: 3.0, -5: 2.66, -4: 2.33, -3: 2.0,
        -2: 1.66, -1: 1.33, 0: 1.0, 1: 0.75,
        2: 0.6, 3: 0.5, 4: 0.428, 5: 0.375, 6: 0.33
    }
    
    def __init__(self, name = "Evasion"):
        super().__init__(name)

    def get_max_stage(self):
        return 6

    def get_min_stage(self):
        return -6