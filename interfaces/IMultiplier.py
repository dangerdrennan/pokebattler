from abc import ABC, abstractmethod

class StatStageBase(ABC):
    STAGE_MULTIPLIERS = {
        -6: 0.25, -5: 0.28, -4: 0.33, -3: 0.4,
        -2: 0.5, -1: 0.66, 0: 1.0, 1: 1.5,
        2: 2.0, 3: 2.5, 4: 3.0, 5: 3.5, 6: 4.0
    }

    def __init__(self, name: str):
        self.stage = 0
        self.name = name

    def raise_stage(self, amount: int = 1):
        self.stage = min(self.get_max_stage(), self.stage + amount)

    def lower_stage(self, amount: int = 1):
        self.stage = max(self.get_min_stage(), self.stage - amount)

    def get_multiplier_value(self):
        return self.STAGE_MULTIPLIERS.get(self.stage, 1.0)

    def reset_stage(self):
        self.stage = 0
        
    def return_neutral(self):
        return self.STAGE_MULTIPLIERS.get(0)

    @abstractmethod
    def get_max_stage(self):
        pass

    @abstractmethod
    def get_min_stage(self):
        pass
