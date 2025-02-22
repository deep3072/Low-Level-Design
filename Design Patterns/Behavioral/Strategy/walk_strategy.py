from travel_strategy import TravelStrategy

class WalkStrategy(TravelStrategy):
    """
    Concrete Strategy: Walk
    """
    def travel(self, origin, destination):
        print(f"Travelling from {origin} to {destination} by walk")