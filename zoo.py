from corral import *


class Zoo:

    def __init__(self):
        self.free_area = 3400
        self.corrals = {}
        self.corrals_count = 0

    def __repr__(self):
        zoo_overview = f'Free area left at zoo: {self.free_area} sq.m.\nTotal corals count: {self.corrals_count}'
        for key, item in self.corrals.items():
            zoo_overview += f'\n{key} corral take {item} sq.m. of total area'
        return zoo_overview

    def create_corral(self, area, kind):
        if self.free_area < area:
            print(f'There is not enough space, available area for new corral: {self.free_area}\n')
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
