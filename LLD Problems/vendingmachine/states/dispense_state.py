from state import State
from coin import Coin
from note import Note

class DispenseState(State):
    def __init__(self, machine):
        self.machine = machine
        print("Vending machine is in Dispense state")

    def click_insert_coin_button(self):
        raise Exception("You cannot click on insert coin button in Dispense state")

    def click_select_item_button(self):
        raise Exception("You cannot click on select item button in Dispense state")

    def insert_coin(self, coin: Coin):
        raise Exception("You cannot insert coin in Dispense state")
    
    def insert_note(self, note: Note):
        raise Exception("You cannot insert note in Dispense state")

    def choose_item(self, code_number: int):
        raise Exception("You cannot choose product in Dispense state")

    def dispense_item(self, code_number: int):
        item = self.machine.inventory.get_item(code_number)
        print(f"Dispensing item - {item.item_name}")
        self.machine.inventory.update_sold_item_count(code_number)
        self.machine.set_vending_machine_state(self.machine.idle_state)
        # return item

    def return_full_money(self):
        raise Exception("You cannot return full money in Dispense state")

    def return_change(self, return_amount: int):
        raise Exception("You cannot get change in Dispense state")