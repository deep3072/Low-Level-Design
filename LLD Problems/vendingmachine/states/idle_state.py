from state import State
from coin import Coin
from note import Note

class IdleState(State):
    def __init__(self, machine):
        self.machine = machine
        print("Vending machine is in idle state")

    def click_insert_coin_button(self):
        self.machine.set_vending_machine_state(self.machine.has_money_state)

    def insert_coin(self, coin: Coin):
        raise Exception("You cannot insert coin in idle state")
    
    def insert_note(self, note: Note):
        raise Exception("You cannot insert note in idle state")

    def click_select_item_button(self):
        raise Exception("Please insert coin first")
    
    def choose_item(self, code_number: int):
        raise Exception("You cannot choose product in idle state")

    def dispense_item(self, code_number: int):
        raise Exception("You cannot dispense product in idle state")

    def return_full_money(self):
        raise Exception("You cannot return full money in idle state")

    def return_change(self, return_amount: int):
        raise Exception("You cannot get change in idle state")