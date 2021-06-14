from .enums import VehicleSize
from .vehicle import Vehicle


class ParkingSpot(object):
    def __init__(self, level: int, row: int, spot_number: int, spot_size: int, vehicle_size: VehicleSize):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle_size = vehicle_size
        self.vehicle = None

    def is_available(self) -> bool:
        return True if self.vehicle else False

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.vehicle:
            return False
        return vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle: Vehicle):
        self.spot_size -= vehicle.spot_size

    def remove_vehicle(self, vehicle: Vehicle):
        self.spot_size += vehicle.spot_size
