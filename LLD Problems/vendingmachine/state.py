from abc import ABC, abstractmethod
from coin import Coin
from note import Note

class State(ABC):
    @abstractmethod
    def click_insert_coin_button(self):
        pass

    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass

    @abstractmethod
    def insert_note(self, note: Note):
        pass

    @abstractmethod
    def click_select_item_button(self):
        pass

    @abstractmethod
    def choose_item(self, code_number: int):
        pass

    @abstractmethod
    def dispense_item(self, code_number: int):
        pass

    @abstractmethod
    def return_full_money(self):
        pass

    @abstractmethod
    def return_change(self, return_amount: int):
        pass
