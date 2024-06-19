#core/ability.py

class Ability:
    def __init__(self, name = 'not implemented'):
        self.name = name
    
    def __str__(self):
        return self.name
    