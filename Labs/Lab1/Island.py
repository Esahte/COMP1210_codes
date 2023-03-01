from random import randint
from AnimalPreditorPrey import Predator, Animal, Prey


class Island:
    """
    Island n X n grid where zero value indicates an unoccupied cell.
    """
    def __init__(self, n, prey_count=0, predator_count=0):
        """Initialize cell to all 0's, then fill with animals """
        print(n, prey_count, predator_count)
        self.animalCount = 0
        self.grid_size = n
        self.grid =[] # [[0]*n for i in range(n)]
        for i in range(n):
            row = [0] * n  # row is a list of n zeros
            self.grid.append(row)
        self.init_animals(prey_count, predator_count)

    def __str__(self):
        """String representation for printing.
        (0,0) will be in the lower left corner. """
        s = ""
        for j in range(self.grid_size - 1, -1, -1):  # print row size1 first
            for i in range(self.grid_size):  # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    s += "{:<2s}".format('.' + " ") # or s += '. '
                else:
                    s += "{:<2s}".format((str(self.grid[i][j])) + " ") # or s += f'{str(grid[i][j])} '
            s += "\n"
        return s

    def register(self, animal):
        self.grid[animal.x][animal.y] = animal
        self.animalCount+=1

    def size(self):
        return self.grid_size**2

    def init_animals(self, prey_count, predator_count):
        while predator_count != 0:
            x, y = randint(0, self.grid_size - 1), randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                wolf = Predator(x, y, self, 'wolf')
                self.register(wolf)
                predator_count -= 1
        while prey_count != 0:
            x, y = randint(0, self.grid_size - 1), randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                moose = Prey(x, y, self, 'moose')
                self.register(moose)
                prey_count -= 1

    def animal(self, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        return 1

    def remove(self, animal):
        self.grid[animal.x][animal.y] = 0
        self.animalCount-=1

    def clear_all_moved_flags(self):
        for i, x in enumerate(self.grid):
            for j in x:
                if isinstance(j, Animal) and j.moved:
                    j.moved = False
