class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops():
        scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
        for scoop in scoops:
            print(scoop.flavor)


class Beverage():
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature
        
def create_beverage():
    beverages = [Beverage("coke"),Beverage("mile", "1"), Beverage("Soda", "3")]
    for beverage in beverages:
        print(beverage.name, beverage.temperature)

class Logfile:
    def __init__(self, filename):
        self.file = open(filename, 'w')
            
    

Logfile("Hello")



