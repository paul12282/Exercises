class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Cage:
    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.cage = []

    def add_animals(self, *animals):
        for animal in animals:
            self.cage.append(animal)

    def __repr__(self):
        output = f'Cage {self.unique_id}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.cage)
        return output


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, '4')


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, '4')


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, '0')


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, '2')


Wolf = Wolf('gray')
Sheep = Sheep('blue')
Snake = Snake('black')
Parrot = Parrot('purple')

c1 = Cage(11)
c1.add_animals(Wolf, Wolf, Snake)
