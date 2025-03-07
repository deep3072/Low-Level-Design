from state import State
from coin import Coin
from note import Note

class HasMoneyState(State):

    def __init__(self, machine):
        self.machine = machine
        print("Vending machine is in HasMoney state")

    def click_insert_coin_button(self):
        pass

    def insert_coin(self, coin: Coin):
        print("Accepted the coin")
        self.machine.add_coin(coin)

    def insert_note(self, note: Note):
        print("Accepted the note")
        self.machine.add_note(note)

    def click_select_item_button(self):
        self.machine.set_vending_machine_state(self.machine.selection_state)

    def choose_item(self, code_number: int):
        raise Exception("You need to click on start product selection button first")

    def dispense_item(self, code_number: int):
        raise Exception("Cannot dispense product in has money state")

    def return_full_money(self):
        # print("Returning full money")
        # machine.set_vending_machine_state(IdleState(machine))
        # return machine.get_coin_list()
        pass

    def return_change(self, return_amount: int):
        raise Exception("Cannot return change in has money state")