from ObjectOriented.Vehicles import Vehicle


class MotorCycle(Vehicle):
    """
    Subclass of *Vehicle* class
    """
    wheels = 2
    no_of_seats = 1

    def vehicle_type(self):
        # noinspection PyCompatibility
        super().vehicle_type()
        return "MotorCycle"
