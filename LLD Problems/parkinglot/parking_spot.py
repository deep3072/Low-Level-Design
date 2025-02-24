from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, id: int, price: int):
        self.id = id
        self.price = price
        self.vehicle = None
        self.is_empty = True

    def park_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_empty = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_empty = True

    def calculate_price(self):
        pass

class TwoWheelerSpot(ParkingSpot):
    def __init__(self, id: int):
        super().__init__(id, 10)

    def calculate_price(self):
        return 10

class FourWheelerSpot(ParkingSpot):
    def __init__(self, id: int):
        super().__init__(id, 20)

    def calculate_price(self):
        return 20