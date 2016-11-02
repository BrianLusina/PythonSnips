class Vehicle(object):
    """
    Vehicle class that is the superclass of all Vehicles in existence
    Attributes:
        name: A String representing the name of the vehicle
        make: String representing the make of the vehicle
        model: String representing the model of the vehicle
        manufacture_year: Integer representing the year of manufacture
        wheels:Integer representing the number of wheels
    """

    def __init__(self, name, make, model, manufacture_year, wheels):
        """
        :return a new vehicle object
        """
        self.name = name
        self.make = make
        self.model = model
        self.manufacture_year = manufacture_year
        self.wheels = wheels


