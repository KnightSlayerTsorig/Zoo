class Animal:
    # class that represent the animal
    def __init__(self, kind, species, area):
        self.kind = kind            # type of the animal(herbivore or predator)
        self.species = species      # kind of the animal
        self.area = area            # amount of the free space needed by the animal to settle in the corral


lion = Animal('predator', "Lion's", 12)
panther = Animal('predator', "Panther's", 12)
lynx = Animal('predator', "Lynx's", 10)
cheetah = Animal('predator', "Cheetah's", 10)
crocodile = Animal('predator', "Crocodile's", 8)
bear = Animal('predator', "Bear's", 7)

horse = Animal('herbivore', "Horse's", 12)
deer = Animal('herbivore', "Deer's", 9)
roe = Animal('herbivore', "Roe's", 5)
monkey = Animal('herbivore', "Monkey's", 2)
racoon = Animal('herbivore', "Racoon's", 1)
rabbit = Animal('herbivore', "Rabbit's", 1)

animal_list = [
    # list of all existing Animal class objects
    lion, panther, lynx, cheetah, crocodile, bear, horse, deer, roe, monkey, racoon, rabbit
]
