class Corral:
    # class that represent the corral
    def __init__(self, number, area, kind):
        self.number = number            # coral number at the zoo
        self.area = area                # total area of the corral
        self.free_area = area           # free area left at the corral
        self.kind = kind                # type of animals that can live in the corral (predator or herbivore)
        self.animals_at_corral = {}     # list of the all animals that live in the corral

    def __repr__(self):
        # magic method that represent corral. In this case it show's all available information about the corral
        corral_overview = f'Corral number: {self.number}\n' \
                          f'Total area taken by corral: {self.area} sq.m.\n' \
                          f'Free area left at the corral: {self.free_area} sq.m.\n' \
                          f'This corral is intended for: {self.kind}.\n' \
                          f'Animals in corral:'
        if len(self.animals_at_corral) > 0:
            for key, item in self.animals_at_corral.items():
                corral_overview += f'\n{key}: {item};'
        else:
            corral_overview += f'\nThere are no animals at this corral\n'
        return corral_overview

    def add_animal(self, kind, species, area, quantity):
        # the method that is responsible for adding animals to the corral
        if kind != self.kind:
            print(f"You can't house {kind} with {self.kind}\n")
        else:
            area_needed = area * quantity
            if area_needed > self.free_area:
                print(f"There is not enough space for {quantity} {species}\n")
            else:
                if species in self.animals_at_corral:
                    self.animals_at_corral[species] += quantity
                else:
                    self.animals_at_corral[species] = quantity
                self.free_area -= area_needed
                print(
                    f'You have successfully added {quantity} {species} to the corral №{self.number}.\n'
                    f'There are {self.free_area} sq.m. of the free space left at the corral\n'
                )
