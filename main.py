from zoo import Zoo
from animals import animal_list
from menu_functions import split, add_animals, info

life_like_a_zoo = Zoo()

running = True
while running:
    print('\nWelcome to my zoo!')
    info()
    action = input('Please enter the number: ')
    if action == '1':
        if life_like_a_zoo.free_area == 0:
            print('Unfortunately there is no free space left at the zoo :(')
        else:
            print(f'Available space: {life_like_a_zoo.free_area} sq.m')
            corral_area = input('Please enter the amount of area that you want to highlight for the corral: ')
            animals_type = input(
                'Please enter the type of the animals that corral is created for\n'
                '1. Herbivore\n'
                '2. Predator\n'
                ':'
            )
            if animals_type == '1':
                life_like_a_zoo.create_corral(int(corral_area), 'herbivore')
            elif animals_type == '2':
                life_like_a_zoo.create_corral(int(corral_area), 'predator')
            else:
                print('Oops,something went wrong...')
    if action == '2':
        if len(life_like_a_zoo.corrals) < 2:
            print(
                "There isn't two corrals at the zoo, if you want to add animals to the corral, you need to "
                "create at least two corrals first"
            )
        else:
            animals = input("Please enter the names of the animals that you want to add: ")
            animals = split(animals)
            add_animals(animal_list, animals, life_like_a_zoo.corrals)
    if action == '3':
        print(life_like_a_zoo)
    if action == '4':
        if life_like_a_zoo.corrals_count < 1:
            print("There is no corrals at the zoo")
        else:
            corral_id = int(input('Please choose corral (enter corral id): '))
            print(life_like_a_zoo.corrals[corral_id])
    if action == '5':
        break
