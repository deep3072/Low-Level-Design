from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    """
    Strategy: Interface for different concrete strategies
    """
    @abstractmethod
    def travel(self, origin, destination):
        pass

