#Vehicle Identification Number - VIN

class Vehicles:
    def __init__(self, modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission):
        self.modelYear = modelYear
        self.totalMileage = totalMileage
        self.vehicleIdentificationNo = VIN
        self.EPAclass = EPAclass
        self.EPAMileage = EPAMileage
        self.engine = engine
        self.transmission = transmission


class Car(Vehicles):
    def __init__(self, modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission, compact, convertibles, fullSize, Hatchback, midSize, subcompact, wagons):
        super().__init__(modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission)
        self.compact = compact
        self.wagons = wagons
        self.subcompact = subcompact
        self.midSize = midSize
        self.Hatchback = Hatchback
        self.fullSize = fullSize
        self.convertibles = convertibles


class Truck(Vehicles):
    def __init__(self, modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission,fullSize, highestHorsepower, midSize, mostFuelEfficient):
        super().__init__(modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission)
        self.fullSize = fullSize
        self.highestHorsepower = highestHorsepower
        self.midSize = midSize
        self.mostFuelEfficient = mostFuelEfficient

class SUV(Vehicles):
    def __init__(self, modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission, twoRow, threeRow, compact, fullSize, midsize, subcompact):
        super().__init__(modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission)
        self.threeRow = threeRow
        self.compact = compact
        self.fullSize = fullSize
        self.midsize = midsize
        self.subcompact = subcompact
        self.twoRow = twoRow

class Minivan(Vehicles):
    def __init__(self, modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission, mostFuelEfficient):
        super().__init__(modelYear, totalMileage, VIN, EPAclass, EPAMileage, engine, transmission)
        self.mostFuelEfficient = mostFuelEfficient