class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.sound}--{self.color} {self.species}, {self.number_of_legs} legs'
           
# class TwoLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color)
#         self.number_of_legs = 2

# class FourLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color)
#         self.number_of_legs = 4

# class ZeroLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color)
#         self.number_of_legs = 0

class Wolf(Animal):
    sound = 'awooo'
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    sound = 'baa'
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    sound = 'hiss'
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    sound = 'Polly wants a cracker!'
    def __init__(self, color):
        super().__init__(color, 2)


print(Wolf("Black"))
print(Sheep("White"))
print(Snake("Red"))
print(Parrot("Blue"))