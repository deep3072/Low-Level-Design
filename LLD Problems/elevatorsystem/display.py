from direction import Direction

class ElevatorDisplay:
    def __init__(self):
        self.floor = 1
        self.direction = Direction.UP

    def show(self):
        print(f"Elevator Display -> Floor: {self.floor}, Direction: {self.direction}")