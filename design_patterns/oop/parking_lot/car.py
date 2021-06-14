from .enums import VehicleSize
from .parking_spot import ParkingSpot
from .vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(vehicle_size=VehicleSize.COMPACT, license_plate=license_plate, spot_size=1)

    def can_fit_in_spot(self, spot: ParkingSpot) -> bool:
        return True if (spot.spot_size == VehicleSize.LARGE or spot.spot_size == VehicleSize.Compact) else False
