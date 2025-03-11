from elevator_car import ElevatorCar
from elevator_controller import ElevatorController
from floor import Floor
from external_button_dispatcher import ExternalButtonDispatcher

class Building:
    def __init__(self, num_floors, num_elevators, elevator_capacity):
        self.elevator_cars = []
        self.elevator_controllers = []
        self.floors = []
        self.external_button_dispatcher = ExternalButtonDispatcher(self.elevator_controllers) # Single external button dispatcher for all floors
        
        # Create elevator cars and their controllers
        for i in range(1, num_elevators + 1):
            elevator = ElevatorCar(i, elevator_capacity)
            self.elevator_cars.append(elevator)
            controller = ElevatorController(elevator)
            self.elevator_controllers.append(controller)
                
        # Create floors
        for i in range(1, num_floors + 1):
            floor = Floor(i, self.external_button_dispatcher)
            self.floors.append(floor)