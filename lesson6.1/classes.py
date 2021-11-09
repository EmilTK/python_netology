import random


class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eating(self, food):
        self.weight += float((food * (10/100)))

    def get_voice(self):
        print(self.voice)


class Poultry(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.name = name
        self.weight = weight

    def collect_eggs(self):
        print(f'{self.name} снесла {random.randint(1, 8)} яйц.')


class Goose(Poultry):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color
        self.voice = 'га-га-га'


class Chiken(Poultry):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'курлы-курлы'


class Duck(Poultry):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'кря-кря'


class Mammals(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def milk(self):
        print(f'{self.name} был(а) подоена.')


class Cow(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'му-му-му'


class Goat(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'бее-беее-бее'


class Sheep(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'бее-беее-бее'

    def cut(self):
        print(f'{self.name} был(а) постиженна.')
