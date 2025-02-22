from travel_strategy import TravelStrategy

class BikeStrategy(TravelStrategy):
    """
    Concrete Strategy: Bike
    """
    def travel(self, origin, destination):
        print(f"Travelling from {origin} to {destination} by Bike")