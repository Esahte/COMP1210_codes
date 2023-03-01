from Island import Island
from AnimalPreditorPrey import Prey,Predator

def main(predator_breed_time, predator_starve_time, initial_predators, prey_breed_teme, initial_prey, size, ticks):
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_teme

    island = Island(size, initial_prey, initial_predators)
    print(island)

    while ticks != 0:
        for i, x in enumerate(island.grid):
            for j in x:
                if isinstance(j, Predator):
                    j.eat()
                elif isinstance(j, Prey):
                    j.escape()
                if isinstance(j, Predator) or isinstance(j, Prey):
                    j.move()
                    j.breed()
                    j.clock_tick()
        island.clear_all_moved_flags()
        print(island)
        ticks -= 1
    print(island.animalCount)


if __name__ == '__main__':
    # predator_breed_time, predator_starve_time, initial_predators, prey_breed_teme, initial_prey, size, ticks
    main(10, 20, 5, 10, 22, 10, 20)
