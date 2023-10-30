pclass Animal:
    def __init__(self, name, lifetime):
        self.name = name
        self.lifetime = lifetime
    
    def __repr__(self):
        return f'Animal(\'{self.name}\', {self.lifetime})'
    
    def __str__(self):
        # freturn f'The creature type is {self.name} and the age is {self.lifetime}'
        return f'Animal(\'{self.name}\', {self.lifetime})'
 