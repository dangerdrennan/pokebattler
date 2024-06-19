# stat_multipliers/crit_stat_stage.py

from interfaces.IMultiplier import StatStageBase

class CritStatStage(StatStageBase):
    STAGE_MULTIPLIERS = {
        -1: 0.0625, 0: 0.125, 1: 0.25, 2: 0.333, 3: 1.0, 4: 1.0
    }
    
    def __init__(self, name = "Critical Hit Probability"):
        super().__init__(name)

    def get_max_stage(self):
        return 3

    def get_min_stage(self):
        return -1
    