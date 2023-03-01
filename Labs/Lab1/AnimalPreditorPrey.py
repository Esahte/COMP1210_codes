from random import shuffle

class Animal:
    def __init__(self, x, y, island, name, moved=False):
        self.moved = moved
        self.x = x
        self.y = y
        self.island = island
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def offsets():
        offsets = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        offsets.extend([(j[0] + 1, j[1] + 1) for i, j in enumerate(offsets)])
        shuffle(offsets)
        return offsets

    def move(self):
        if not self.moved:
            for i in self.offsets():
                x, y = self.x + i[0], self.y + i[1]
                if not self.island.animal(x, y):
                    self.island.remove(self)
                    self.x, self.y = x, y
                    self.island.register(self)
                    break
            self.moved=True

    def check_grid(self, type_looking_for):
        for i in self.offsets():
            x, y = self.x + i[0], self.y + i[1]
            if isinstance(self.island.animal(x, y), type_looking_for):
                return self.island.animal(x, y)
        return 0


"""THIS IS THE PREDATOR CLASS"""
class Predator(Animal):
    def __init__(self, x, y, island, name, moved=False):
        super().__init__(x, y, island, name, moved)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time

    def breed(self):
        if self.breed_clock <= 0:
            if self.check_grid(int):
                self.breed_clock = self.breed_time
                baby_animal = Predator(0, 1, self.island, 'baby_wolf')
                self.island.register(baby_animal)

    def eat(self):
        if not self.moved:
            prey = self.check_grid(Prey)
            if prey:
                x, y = prey.x, prey.y
                self.island.remove(prey)
                self.island.remove(self)
                self.x, self.y = x, y
                self.island.register(self)
                self.starve_clock = self.starve_time
                self.moved=True

    def clock_tick(self):
        self.breed_clock -= 1
        self.starve_clock -= 2
        if self.starve_clock <= 0:
            self.island.remove(self)

"""THIS IS THE PREY CLASS"""
class Prey(Animal):
    def __init__(self, x, y, island, name, moved=False):
        super().__init__(x, y, island, name, moved)
        self.breed_clock = self.breed_time

    def breed(self):
        if self.breed_clock <= (self.breed_time // 2):
            if self.check_grid(int):
                self.breed_clock = self.breed_time
                baby_animal = Prey(0, 1, self.island, 'baby_moose')
                self.island.register(baby_animal)

    def clock_tick(self):
        self.breed_clock -= 5

    def escape(self):
        if not self.moved:
            if self.check_grid(Predator):
                self.move()
                self.moved=True