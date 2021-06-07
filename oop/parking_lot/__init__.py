from typing import Union

from .enums import VehicleSize
from .enums import VehicleSize
from .parking_spot import ParkingSpot
from .vehicle import Vehicle


class ParkingLot(object):
    def __init__(self, num_levels: int):
        self.num_levels = num_levels
        self.levels = []

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False


class Level(object):
    SPOTS_PER_ROW = 10

    def __init__(self, floor: int, total_spots: int):
        self.floor = floor
        self.num_spots = total_spots
        self.available_spots = 0
        self.parking_spots = []

    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle: Vehicle) -> Union[ParkingSpot, None]:
        spot = self._find_available_spot(vehicle)
        if not spot:
            return None
        else:
            spot.park_vehicle(vehicle)
            return spot

    def _find_available_spot(self, vehicle: Vehicle) -> Union[ParkingSpot, None]:
        """Find an available spot where vehicle can fit, or return None"""
        pass

    def _park_starting_at_spot(self, spot: ParkingSpot, vehicle: Vehicle):
        """Occupy starting at spot.spot_number to vehicle.spot_size."""
        # ...
