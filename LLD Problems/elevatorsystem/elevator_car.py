from status import Status
from direction import Direction
from display import ElevatorDisplay
from internal_buttons import InternalButtons

class ElevatorCar:
    def __init__(self, id, capacity: int):
        self.id = id
        self.capactiy = capacity
        self.current_floor = 1
        self.elevator_status = Status.IDLE
        self.elevator_direction = Direction.UP
        self.display = ElevatorDisplay()
        self.internal_buttons = InternalButtons()

    def move(self, destination_floor: int, direction: Direction):
        print(f"\n[Elevator {self.id}]: Moving from floor {self.current_floor} to {destination_floor} [{direction.name}]")
        self.elevator_status = Status.MOVING
        self.elevator_direction = direction
        
        # Elevator moved to destination floor
        self.current_floor = destination_floor
        self.display.floor = destination_floor
        self.display.direction = direction
        self.display.show()
        self.elevator_status = Status.IDLE
        print(f"[Elevator {self.id}]: Arrived at floor {self.current_floor}\n")