class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):

    def __init__(self, color):
        super().__init__(color, 2)


class Cage():

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


class NoColorsPassedError(Exception):
    pass


class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        output = f'{__class__.__name__}\n'
        output +=  '\n'.join(str(one_cage)
                         for one_cage in self.cages)
        return output

    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]

    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)
          
    def get_animals(self, **kwargs):
        print(f'{kwargs=}')
        return [one_animal for one_cage in self.cages
                    for one_animal in one_cage.animals
                        if (('color' in kwargs and one_animal.color == kwargs['color']) and
                            ('legs' in kwargs and one_animal.number_of_legs == kwargs['legs']))]

wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('green')
snake = Snake('brown')
parrot1 = Parrot('pink')
parrot2 = Parrot('green')
c1 = Cage(1)
c1.add_animals(sheep1, parrot1)
c2 = Cage(2)
c2.add_animals(sheep2, parrot2)
z1 = Zoo()
z1.add_cages(c1, c2)
# z2 = Zoo()
# c3 = Cage(3)
# z2.add_cages(c3)
# z1.transfer_animal(z2, sheep1)
print(z1)
# print(z2)
print(z1.animals_by(color="white", legs=4))