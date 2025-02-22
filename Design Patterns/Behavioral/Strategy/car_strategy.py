from travel_strategy import TravelStrategy

class CarStrategy(TravelStrategy):
    """
    Concrete Strategy: Car
    """
    def travel(self, origin, destination):
        print(f"Travelling from {origin} to {destination} by Car")