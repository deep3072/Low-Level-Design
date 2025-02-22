from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Product Abstact Class: Declares the operations that all concrete products must implement.
    """
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    """
    Concrete Product 1: Implements the Product interface with Car functionality.
    """
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self): # Concrete product 2
        return "Riding a bike"

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
    
def client_code(factory):
    """
    The client code accepts any factory subclass and calls its create_vehicle method. This pattern decouples the client from specific product classes (Car, Bike) and works with products through the Vehicle common interface.
    """
    vehicle = factory.create_vehicle()
    print(vehicle.drive())
    
car_factory = CarFactory()
bike_factory = BikeFactory()

client_code(car_factory)
client_code(bike_factory)