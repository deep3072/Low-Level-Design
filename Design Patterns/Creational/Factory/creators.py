from abc import ABC, abstractmethod
from car import Car
from bike import Bike

class VehicleFactory(ABC):
    """
    Creator Abstact class: Returns an object of Product class.
    """
    @abstractmethod
    def create_vehicle(self):
        """
        Factory method: Will be overridden by concrete factories to return specific products. 
        Can also provide some default implementation.
        """
        pass

    def some_operation(self):
        """
        Creator can also contain some business logic that relies on Product object, returned by factory method. 
        Subclasses can indirectly change this business logic by overriding the factory method and returning 
        a different type of product from it.
        """
        product = self.create_vehicle()
        result = f"Some action: {product.operation()}"
        return result
    
class CarFactory(VehicleFactory):
    """
    Concrete Creator 1: override the factory method to create and return Car instance.
    """
    def create_vehicle(self):
        return Car()
    
class BikeFactory(VehicleFactory):
    def create_vehicle(self): # Concrete Creator 2
        return Bike()    