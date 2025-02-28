class Vehicle:
    def get_interior_width(self):
        interior_width = 10 # default width
        return interior_width

class Car(Vehicle):
    def get_interior_width(self):
        cabin_width = 15 # logic to calculate car interior width
        return cabin_width

class RacingCar(Vehicle):
    def get_interior_width(self):
        cockpit_width = 5 # logic to calculate racing car cockpit width
        return cockpit_width

class vehicle_utils:
    def main(self):
        first = Car()
        second = Car()
        third = RacingCar()
        
        myCars = [first, second, third]
        for car in myCars:
            print(car.get_interior_width()) # This will work correctly for all types of cars.
            
"""
Changed the design hierarchy structure for the classes to make it more LSP compliant.
"""