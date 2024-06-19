# stat_multipliers/standard_stat_stage.py

from interfaces.IMultiplier import StatStageBase

class StandardStatStage(StatStageBase):
    
    def __init__(self, name = "Standard Stat"):
        super().__init__(name)

    def get_max_stage(self):
        return 6

    def get_min_stage(self):
        return -6