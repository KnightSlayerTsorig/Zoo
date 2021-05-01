def split(animals):
    # function that split user input
    return animals.replace(' ', '').lower().split(',')


def add_animals(a_list, a_to_add_list, corrals):
    # function that allows user add animals to existing corrals
    for el in corrals:
        if corrals[el].kind == 'herbivore':
            herb = corrals[el]
        if corrals[el].kind == 'predator':
            pred = corrals[el]
    for i in a_list:
        for j in a_to_add_list:
            if j + "'s" == i.species.lower():
                if i.kind == herb.kind:
                    herb.add_animal(i.kind, j, i.area, 1)
                if i.kind == pred.kind:
                    pred.add_animal(i.kind, j, i.area, 1)
            else:
                pass


def info():
    # function that displays on the screen actions that user can perform
    print(
        'Enter the number of the action you want to perform:\n'
        '1. Create a new corral at the zoo\n'
        '2. Add animal(s) to the existing corral\n'
        '3. Get overall zoo info\n'
        '4. Get overall corrals info\n'
        '5. Exit\n'
    )
