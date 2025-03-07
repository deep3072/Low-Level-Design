from state import State
from coin import Coin
from note import Note

class SelectionState(State):
    def __init__(self, machine):
        self.machine = machine
        print("Vending machine is in Selection state")

    def click_insert_coin_button(self):
        raise Exception("You cannot click on insert coin button in selection state")

    def click_select_item_button(self):
        pass

    def insert_coin(self, coin: Coin):
        raise Exception("You cannot insert coin in selection state")
    
    def insert_note(self, note: Note):
        raise Exception("You cannot insert note in selection state")

    def choose_item(self, code_number: int):
        is_item_available = self.machine.inventory.is_item_available(code_number)

        if not is_item_available:
            print("Item not available")
            return
        
        user_paid = self.machine.total_payment
        item = self.machine.inventory.get_item(code_number)

        if user_paid < item.price:
            print("\n")
            print("Insufficient amount paid.")
            print(f"You selected {item.item_name} which costs {item.price} and you paid {user_paid}")
            self.return_full_money()
        else:
            if user_paid > item.price:
                self.return_change(user_paid-item.price)
            
            self.machine.set_vending_machine_state(self.machine.dispense_state)
            self.machine.dispense_item(code_number)

    def dispense_item(self, code_number: int):
        raise Exception("Cannot dispense item in selection state")

    def return_full_money(self):
        print("Returning full money")
        self.machine.set_vending_machine_state(self.machine.idle_state)
        print(f"Returning ${self.machine.total_payment} in the coin dispense tray")

    def return_change(self, return_amount: int):
        print(f"Returning change in the coin dispense tray: ${return_amount}")