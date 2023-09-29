class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    #class attribute
    max_scoops = 3
    def __init__(self):
        #instance attribute
        self.scoops = []
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
    
class Person():
    population = 0
    def __init__(self, name):
        Person.population +=1
    
    def __del__(self):
        Person.population -=1
      

class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount


                
t1 = Transaction(1000)
t2 = Transaction(-500)
print(Transaction.balance)
        
     