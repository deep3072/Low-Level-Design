from direction import Direction
from status import Status
from abc import ABC, abstractmethod

class ElevatorAssignmentStrategy(ABC):
    @abstractmethod
    def assign_elevator(self, elevator_controllers, destination_floor, direction):
        pass

class DynamicElevatorAssignmentStrategy(ElevatorAssignmentStrategy):
    # penalty based algorithm to get best possible elevator
    def assign_elevator(self, elevator_controllers, destination_floor, direction):
        best_controller = None
        best_score = float('inf')
        
        for controller in elevator_controllers:
            elevator = controller.elevator_car
            if elevator.elevator_status != Status.IDLE:
                if elevator.elevator_direction == direction:
                    if (direction == Direction.UP and elevator.current_floor <= destination_floor) or \
                       (direction == Direction.DOWN and elevator.current_floor >= destination_floor):
                        score = abs(destination_floor - elevator.current_floor)
                    else:
                        score = abs(destination_floor - elevator.current_floor) + 10  # penalty if passed
                else:
                    score = abs(destination_floor - elevator.current_floor) + 20  # penalty for wrong direction
            else:
                score = abs(destination_floor - elevator.current_floor)
            
            if score < best_score:
                best_score = score
                best_controller = controller
        
        return best_controller
    

class OddEvenElevatorAssignmentStrategy(ElevatorAssignmentStrategy):
    pass

class FixedFloorElevatorAssignmentStrategy(ElevatorAssignmentStrategy):
    pass