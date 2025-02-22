from travel_strategy import TravelStrategy

class Navigator:
    """
    Context: Navigator class that has-a strategy
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self._strategy = strategy

    def build_route(self, origin, destination):
        self._strategy.travel(origin, destination)
        