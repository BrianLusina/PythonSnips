from pprint import pprint

from ObjectOriented.Vehicles import motor_cycle


class Kawasaki(motor_cycle.MotorCycle):
    """
    Child class of Motorcycle
    """

    def vehicle_type(self):
        # noinspection PyCompatibility
        return super().vehicle_type()


kawasaki = Kawasaki("Kawasaki", "Kawasaki Spyder", "Spyder25", 2000, 5000000, "2500CC")
pprint(kawasaki.__repr__())
