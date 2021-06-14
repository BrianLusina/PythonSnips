from .enums import VehicleSize
from .parking_spot import ParkingSpot
from .vehicle import Vehicle


class Bus(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(vehicle_size=VehicleSize.LARGE, license_plate=license_plate, spot_size=5)

    def can_fit_in_spot(self, spot: ParkingSpot) -> bool:
        return True if spot.spot_size == VehicleSize.LARGE else False
