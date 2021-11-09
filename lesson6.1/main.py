from classes import Poultry, Mammals, Goose, Cow, Sheep, Chiken, Goat, Duck
import random


def main():
    gray = Goose('Серый', 5, 'gray')
    white = Goose('Белый', 7, 'white')
    manika = Cow('Манька', 150)
    barshek = Sheep('Барашек', 70)
    kudraviy = Sheep('Кудрявый', 75)
    koko = Chiken('Ко-Ко', 2)
    kykareky = Chiken('Кукареку', 3)
    roga = Goat('Рога', 53)
    kopyta = Goat('Копыта', 62)
    krakva = Duck('Кряква', 8)

    animals = [gray, white, manika, barshek, kudraviy, koko, kykareky,
               roga, kopyta, krakva]

    def interaction():
        for animal in animals:
            animal.eating(random.randint(20, 150))
            print(f'Вес {animal.name}: {animal.weight}')

            if isinstance(animal, Poultry):
                animal.collect_eggs()
            elif isinstance(animal, Mammals):
                animal.milk()
            elif isinstance(animal, Sheep):
                animal.cut()

    interaction()


main()
