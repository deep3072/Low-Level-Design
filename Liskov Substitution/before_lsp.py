class Car:
    def __init__(self):
        pass
    
    def get_cabin_width(self):
        cabin_width = 10 # logic to calculate cabin width
        return cabin_width
    
class RacingCar(Car):
    def get_cabin_width(self):
        raise NotImplementedError("RacingCar does not have a cabin")
    
    def get_cockpit_width(self):
        cockpit_width = 5 # logic to calculate cockpit width
        return cockpit_width
    
class car_utils:
    def main(self):
        first = Car()
        second = Car()
        third = RacingCar()
        
        myCars = [first, second, third]
        for car in myCars:
            print(car.get_cabin_width()) # This will throw an error for RacingCar. It will not work correctly.

"""
This does not go well with LSP because RacingCar does not have a cabin and hence the method getCabinWidth should not be called on RacingCar.
"""