from inventory import Inventory
from coin import Coin
from note import Note
from state import State
from states.idle_state import IdleState
from states.has_money_state import HasMoneyState
from states.dispense_state import DispenseState
from states.selection_state import SelectionState

class VendingMachine:
    def __init__(self):
        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispense_state = DispenseState(self)
        self.selection_state = SelectionState(self)
        self.current_state = self.idle_state
        self.inventory = Inventory()
        self.total_payment = 0

    def set_vending_machine_state(self, state: State):
        self.current_state = state

    def click_insert_coin_button(self):
        self.current_state.click_insert_coin_button()

    def insert_coin(self, coin: Coin):
        self.current_state.insert_coin(coin)

    def add_coin(self, coin: Coin):
        self.total_payment += coin.value

    def insert_note(self, note: Note):
        self.current_state.insert_note(note)

    def add_note(self, note: Note):
        self.total_payment += note.value

    def click_select_item_button(self):
        self.current_state.click_select_item_button()

    def choose_item(self, code_number: int):
        self.current_state.choose_item(code_number)

    def dispense_item(self, code_number: int):
        self.current_state.dispense_item(code_number)

    def fill_inventory(self):
        self.inventory.fill_inventory(self)

    def show_inventory(self):
        self.inventory.show_inventory(self)