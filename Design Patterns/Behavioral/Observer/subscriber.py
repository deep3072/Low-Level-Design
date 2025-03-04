from abc import ABC, abstractmethod

class Subscriber(ABC):
    """
    Observer interface: declare update method to be called by the publisher
    """
    @abstractmethod
    def update(self, temperature: float):
        pass