from creators import CarFactory, BikeFactory

def client_code(factory):
    """
    The client code accepts any factory subclass and calls its create_vehicle method. 
    This pattern decouples the client from specific product classes (Car, Bike) and works with products through the Vehicle common interface.
    """
    vehicle = factory.create_vehicle()
    print(vehicle.drive())
    
car_factory = CarFactory()
bike_factory = BikeFactory()

client_code(car_factory)
client_code(bike_factory)