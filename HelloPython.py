class Monster:
     def __init__(self,health,energy):
          self.health = health
          self.energy = energy
     
     def update_energy(self,amount):
          self.energy += amount
     
     def get_damage(self,amount):
          self.energy -= amount

#1. create a hero class with 2 parameters: damage, monster
class Hero:
     def __init__(self,damage,monster):
          self.damage = damage
          self.monster = monster
#3. the hero class should have an attack method that calls the get_demage method
# the amount of damage is hero.damage
     def attack(self):
          self.monster.get_damage(self.damage)
          
monster = Monster(health =100, energy = 50)
hero = Hero(damage =15, monster= monster)

print(monster.health)
hero.attack()
print(monster.health)          
               