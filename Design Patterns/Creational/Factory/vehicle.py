from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Product Abstact Class: Declares the operations that all concrete products must implement.
    """
    @abstractmethod
    def drive(self):
        pass
