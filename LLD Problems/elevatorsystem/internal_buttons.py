from internal_button_dispatcher import InternalButtonDispatcher

class InternalButtons:
    def __init__(self):
        self.internal_button_dispatcher = InternalButtonDispatcher()

    def press_button(self, destination_floor, elevator_controller):
        print(f"[Internal Button] In Elevator {elevator_controller.elevator_car.id}: Button for floor {destination_floor} pressed.")
        self.internal_button_dispatcher.submit_request(elevator_controller, destination_floor)