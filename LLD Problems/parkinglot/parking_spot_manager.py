from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingSpotManager:

    def __init__(self, parking_spots: List[ParkingSpot]):
        self.parking_spots = parking_spots

    def find_parking_spot(self, vehicle: Vehicle): 
        for spot in self.parking_spots:
            if spot.is_empty:
                return spot
        return "No parking spot available"

    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if spot.is_empty:
                spot.park_vehicle(vehicle)
                return f"Vehicle {vehicle.vehicle_number} parked at spot {spot.id}"
        return "No parking spot available"

    def remove_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if not spot.is_empty and spot.vehicle == vehicle:
                spot.remove_vehicle()
                return spot
        return None
    
    # to increase the capacity of parking lot
    def add_parking_spots(self, parking_spots: List[ParkingSpot]):
        self.parking_spots.extend(parking_spots)

    def display_parking_spots(self):
        for spot in self.parking_spots:
            print(f"Spot ID: {spot.id}, Type: {spot.__class__.__name__}, Vehicle: {spot.vehicle.vehicle_number if spot.vehicle else None}, Price: {spot.price}")

    # def remove_parking_spot(self, parking_spot: ParkingSpot):
    #     pass

class TwoWheelerSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots: List[ParkingSpot]):
        super().__init__(parking_spots)

class FourWheelerSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots: List[ParkingSpot]):
        super().__init__(parking_spots)