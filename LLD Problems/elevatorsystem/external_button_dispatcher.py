from elevator_assignment_strategy import DynamicElevatorAssignmentStrategy

class ExternalButtonDispatcher:
    def __init__(self, elevator_controllers, assignment_strategy=None):
        self.elevator_controllers = elevator_controllers
        if assignment_strategy is None:
            self.assignment_strategy = DynamicElevatorAssignmentStrategy()
        else:
            self.assignment_strategy = assignment_strategy

    def submit_request(self, destination_floor, direction):
        print(f"[External Request] Received call at floor {destination_floor} for direction {direction.name}")
        best_controller = self.assignment_strategy.assign_elevator(self.elevator_controllers, destination_floor, direction)
        
        if best_controller is None:
            best_controller = self.elevator_controllers[0]
            print(f"[External Dispatcher] No elevator available; defaulting to Elevator {best_controller.elevator_car.id}.")
        else:
            print(f"[External Dispatcher] Elevator {best_controller.elevator_car.id} assigned for this request.")
        
        best_controller.submit_new_request(destination_floor, direction)
        best_controller.control_elevator_car()
        # Return the assigned elevator controller so it can be used later for internal requests.
        return best_controller
