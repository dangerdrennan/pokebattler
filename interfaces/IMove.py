# interfaces/IMove.py

from abc import ABC, abstractmethod

class MoveInterface(ABC):
    
    @abstractmethod
    def apply_move(self, attacker, targets, field, history):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_move_type(self):
        pass

    @abstractmethod
    def get_move_category(self):
        pass  # Physical, Special, or Status

    @abstractmethod
    def get_pp(self):
        pass
    
    @abstractmethod
    def get_primary_accuracy(self):
        pass
    
    @abstractmethod
    def get_secondary_accuracy(self):
        pass

    @abstractmethod
    def get_priority(self):
        pass
    
    @abstractmethod
    def get_status_effect(self):
        pass
    
    @abstractmethod
    def get_secondary_effect(self):
        pass
    
    @abstractmethod
    def get_modified_accuracy(self):
        pass