from direction import Direction

class InternalButtonDispatcher:
    def __init__(self):
        pass

    def submit_request(self, elevator_controller, destination_floor):
        print(f"[Internal button Request] Elevator {elevator_controller.elevator_car.id} requested to go to floor {destination_floor}")
        current_floor = elevator_controller.elevator_car.current_floor
        direction = Direction.UP if destination_floor > current_floor else Direction.DOWN
        elevator_controller.submit_new_request(destination_floor, direction)
        elevator_controller.control_elevator_car()