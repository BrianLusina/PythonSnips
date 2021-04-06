from pprint import pprint

from ObjectOriented.Vehicles import car


class Jeep(car.Car):
    def vehicle_type(self):
        # noinspection PyCompatibility
        return super().vehicle_type()


jeep = Jeep("Jeep", "SUV", "Cherokee", 2000, 500000, "6000CC")
pprint(jeep.vehicle_type())
pprint(jeep.__repr__())
