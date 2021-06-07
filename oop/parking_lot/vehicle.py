from abc import ABC, abstractmethod

from .enums import VehicleSize
from .parking_spot import ParkingSpot


class Vehicle(ABC):
    def __init__(self, vehicle_size: VehicleSize, license_plate: str, spot_size: int):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_token = []

    def clear_spots(self):
        for spot in self.spots_token:
            spot.remove_vehicle(self)

    def take_spot(self, spot):
        self.spots_token.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot: ParkingSpot) -> bool:
        raise NotImplementedError("Not Yet Implemented")
