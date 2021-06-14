from .enums import VehicleSize
from .vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(vehicle_size=VehicleSize.MOTORCYCLE, license_plate=license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True
