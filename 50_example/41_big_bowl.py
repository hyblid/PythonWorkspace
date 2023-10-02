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

#BigBowl <- Bowl <- Scoop
class BigBowl(Bowl):
    max_scoops = 5
    
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
# s4 = Scoop('flavor 4')
# s5 = Scoop('flavor 5')
# bb = BigBowl()
# bb.add_scoops(s1, s2)
# bb.add_scoops(s3)
# bb.add_scoops(s4, s5)
# print(bb)    
    
class NotEnoughPostageError(Exception):
    pass

class Envelope:
    postage_multiplier = 10

    def __init__(self, weight):
        self.weight = weight
        self.postage = 0
        self.was_sent = False

    def add_postage(self, amount):
        self.postage += amount

    def send(self):
        if self.postage >= self.weight * self.postage_multiplier:
            self.was_sent = True
        else:
            raise NotEnoughPostageError('Not enough postage')

class BigEnvelop(Envelope):
    postage_multiplier = 15
 
"""
Create a Phone class that represents a mobile phone. (Are there still nonmobile
phones?) The phone should implement a dial method that dials a phone number
(or simulates doing so). Implement a SmartPhone subclass that uses the
Phone.dial method but implements its own run_app method. Now implement
an iPhone subclass that implements not only a run_app method, but also its
own dial method, which invokes the parent’s dial method but whose output is
all in lowercase as a sign of its coolness."""       

class Phone:
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'

class SmartPhone(Phone):
    def run_app(self, app_name):
        return f'Running an app: {app_name}'

class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()
        
s = SmartPhone()
print(s.run_app("smart"))
        
"""
Define a Bread class representing a loaf of bread. We should be able to invoke a
get_nutrition method on the object, passing an integer representing the
number of slices we want to eat. In return, we’ll receive a dict whose key-value
pairs will represent calories, carbohydrates, sodium, sugar, and fat, indicating
the nutritional statistics for that number of slices. Now implement two new
classes that inherit from Bread, namely WholeWheatBread and RyeBread. Each
class should implement the same get_nutrition method, but with different
nutritional information where appropriate."""

class Bread:
    def __init__(self):
        # nutrition per slice
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8
    #The vars() function returns the __dict__ attribute of an object
    def get_nutrition(self, number_of_slices):
        return {key: value*number_of_slices
                for key, value in vars(self).items()}
    
class WholeWheatBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 138
        self.sugar = 1.4
        self.fat = 1   
    
class RyeBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 172
        self.sugar = 1
        self.fat = 0.8
    
r = RyeBread()
print(r.get_nutrition(10))