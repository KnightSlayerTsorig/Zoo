from corral import *


class Zoo:
    # class that represent zoo
    def __init__(self):
        self.free_area = 3400       # total area of the zoo (square meters)
        self.corrals = {}           # list of the corrals that available at the zoo
        self.corrals_count = 0      # amount of the corrals at the zoo

    def __repr__(self):
        # magic method that represent zoo. In this case it show's all available information about the zoo
        zoo_overview = f'Free area left at zoo: {self.free_area} sq.m.\nTotal corals count: {self.corrals_count}'
        for key, item in self.corrals.items():
            zoo_overview += f'\n{key} {item} '
        return zoo_overview

    def create_corral(self, area, kind):
        # method that can create new objects of the Corral class and add them to the zoo
        if self.free_area < area:
            print(f'There is not enough space, available area for new corral: {self.free_area} sq.m.\n')
        else:
            self.corrals_count += 1
            self.free_area -= area
            new_corral = Corral(self.corrals_count, area, kind)
            self.corrals[self.corrals_count] = new_corral
            print(
                f'You successfully create new corral.\n'
                f'Corral №{self.corrals_count}\n'
                f'Total corral area: {area} sq.m.\n'
                f'Animals type: {kind}\n'
            )
