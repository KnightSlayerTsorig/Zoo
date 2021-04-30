class Animal:

    def __init__(self, kind, species, area):
        self.kind = kind
        self.species = species
        self.area = area


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
    lion, panther, lynx, cheetah, crocodile, bear, horse, deer, roe, monkey, racoon, rabbit
]
