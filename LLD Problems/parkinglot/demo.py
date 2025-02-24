from parking_spot import TwoWheelerSpot, FourWheelerSpot
from vehicle import Vehicle
from vehicle_type import VehicleType
from parking_spot_manager import ParkingSpotManager, TwoWheelerSpotManager, FourWheelerSpotManager

class Demo:
    def run():
        two_wheeler_parking = TwoWheelerSpotManager([TwoWheelerSpot(id) for id in range(1, 6)])
        four_wheeler_parking = FourWheelerSpotManager([FourWheelerSpot(id) for id in range(6, 11)])

        car1 = Vehicle("ABC123", VehicleType.FOUR_WHEELER)
        car2 = Vehicle("XYZ123", VehicleType.FOUR_WHEELER)
        bike1 = Vehicle("PQR123", VehicleType.TWO_WHEELER)

        print(four_wheeler_parking.park_vehicle(car1))
        print(four_wheeler_parking.park_vehicle(car2))
        print(two_wheeler_parking.park_vehicle(bike1))

        two_wheeler_parking.display_parking_spots()
        four_wheeler_parking.display_parking_spots()

        
if __name__ == "__main__":
    Demo.run()
