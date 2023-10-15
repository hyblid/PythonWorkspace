class Monster:
    #Class attribute - global
    # health = 50
    # energy = 100
    
    #this call super for Monster and Fish by kwargs
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
    
    def attack(self, amount):
        print("The monster has attached")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        
    def move(self, speed):
        print("The monster has moveed")
        print(f"It has a speed of {speed}")
        
class Fish:
    #kwargs is empty but for extention
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
        
    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")        

#MRO (Method Resolution Order)
class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)

# should be kwargs
shark = Shark(bite_strength= 50, health= 200, energy= 55, speed=120, has_scales= False)
print(shark.speed)
print(shark.has_scales)
