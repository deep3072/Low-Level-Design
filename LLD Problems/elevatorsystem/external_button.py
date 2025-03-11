from direction import Direction
from external_button_dispatcher import ExternalButtonDispatcher

class ExternalButton:
    def __init__(self, dispatcher: ExternalButtonDispatcher):
        self.external_button_dispatcher = dispatcher
    
    def press_button(self, destination_floor, direction: Direction):
        print(f"[External Button] Button pressed at floor {destination_floor} for direction {direction.name}")
        # Return the controller assigned by external dispatcher
        return self.external_button_dispatcher.submit_request(destination_floor, direction)