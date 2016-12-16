from ObjectOriented.Vehicles import car
from pprint import pprint


class Jeep(car.Car):
    def vehicle_type(self):
        return super().vehicle_type()


jeep = Jeep("Jeep", "SUV", "Cherokee", 2000, 500000, "6000CC")
pprint(jeep.vehicle_type())
pprint(jeep.__repr__())

