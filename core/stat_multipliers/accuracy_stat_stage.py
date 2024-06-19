# stat_multipliers/accuracy_stat_stage.py

from interfaces.IMultiplier import StatStageBase

class AccuracyStatStage(StatStageBase):
    
    STAGE_MULTIPLIERS = {
        -6: 0.33, -5: 0.375, -4: 0.428, -3: 0.5,
        -2: 0.6, -1: 0.75, 0: 1.0, 1: 1.33,
        2: 1.66, 3: 2.0, 4: 2.33, 5: 2.66, 6: 3.0
    }
    
    def __init__(self, name = "Accuracy"):
        super().__init__(name)

    def get_max_stage(self):
        return 6

    def get_min_stage(self):
        return -6
    