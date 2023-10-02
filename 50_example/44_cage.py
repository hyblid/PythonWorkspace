class Animal():
    def __init__(self, number_of_legs):
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    space_required = 10
    def __init__(self):
        super().__init__(4)

class Sheep(Animal):
    space_required = 5
    def __init__(self):
        super().__init__(4)

class Snake(Animal):
    space_required = 2
    def __init__(self):
        super().__init__(0)


class Parrot(Animal):
    space_required = 1
    def __init__(self):
        super().__init__(2)


class NotEnoughSpaceError(Exception):
    pass

class DangerousAssignmentError(Exception):
    pass

animal_safety = {Wolf: [Wolf, Snake, Parrot],
                 Sheep: [Sheep, Snake, Parrot],
                 Snake: [Wolf, Sheep],
                 Parrot: [Wolf, Sheep]}

class Cage():

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            for one_current_resident in self.animals:
                if type(one_animal) not in animal_safety[type(one_current_resident)]:
                    raise DangerousAssignmentError(
                        f'You cannot put a {type(one_animal)} with a {type(one_current_resident)}!')
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output

class BigCage(Cage):
    max_animals = 5
        
wolf = Wolf()
sheep = Sheep()
snake = Snake()
parrot = Parrot()
c1 = Cage(1)
c1.add_animals(parrot, snake)
print(c1)

