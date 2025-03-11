from external_button import ExternalButton

class Floor:
    def __init__(self, floor_number, external_button_dispatcher):
        self.floor_number = floor_number
        self.external_button = ExternalButton(external_button_dispatcher)