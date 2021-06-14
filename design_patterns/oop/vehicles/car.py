from ObjectOriented.Vehicles import Vehicle


class Car(Vehicle):
    """
    Car class which is a subclass of *Vehicle*
    """
    wheels = 4
    no_of_seats = 4

    def vehicle_type(self):
        # noinspection PyCompatibility
        super().vehicle_type()
        return "Car"
