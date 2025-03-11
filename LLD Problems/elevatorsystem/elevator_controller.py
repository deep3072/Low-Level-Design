from elevator_car import ElevatorCar
from direction import Direction

class ElevatorController:
    def __init__(self, elevator_car: ElevatorCar):
        self.elevator_car = elevator_car
        self.pending_requests = []  # (destination_floor, direction)

    def submit_new_request(self, destination_floor, direction):
        print(f"[ElevatorController] Received request for floor {destination_floor} [{direction.name}] for Elevator {self.elevator_car.id}")
        self.pending_requests.append((destination_floor, direction))
    
    def control_elevator_car(self):
        if not self.pending_requests:
            print(f"[ElevatorController] No pending requests for Elevator {self.elevator_car.id}.")
            return
        
        # sort the pending requests based on the first request's direction.
        first_direction = self.pending_requests[0][1]
        if first_direction == Direction.UP:
            # 2 heaps can also be used to optimize this
            self.pending_requests.sort(key=lambda x: x[0])
        else:
            self.pending_requests.sort(key=lambda x: x[0], reverse=True)
        
        while self.pending_requests:
            destination_floor, direction = self.pending_requests.pop(0)
            self.elevator_car.move(destination_floor, direction)