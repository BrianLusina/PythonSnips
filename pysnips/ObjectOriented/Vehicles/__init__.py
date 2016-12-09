from abc import ABCMeta, abstractmethod


class Vehicle(object):
    """
    Vehicle class that is the superclass of all Vehicles in existence
    This class is abstract meaning there should not be an instance of this class, but rather an instance of its child
     classes
    Attributes:
        name: A String representing the name of the vehicle
        make: String representing the make of the vehicle
        model: String representing the model of the vehicle
        manufacture_year: Integer representing the year of manufacture
        price: float representing the price of the vehicle
    """

    # defines this class as abstract
    __metaclass__ = ABCMeta

    wheels = 0
    no_of_seats = 1

    def __init__(self, name, make, model, manufacture_year, price, engine_capacity):
        """
        :return a new vehicle object
        """
        self.name = name
        self.make = make
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        self.engine_capacity = engine_capacity

    @abstractmethod
    def vehicle_type(self):
        """Returns the type of vehicle this is"""
        pass

    def __repr__(self, *args, **kwargs):
        return "Name: %r, Make: %r, Model: %r, Manufacture Year: %r Price: %r, Engine Capacity: %r" % (
            self.name, self.make, self.model, self.manufacture_year, self.price, self.engine_capacity)
