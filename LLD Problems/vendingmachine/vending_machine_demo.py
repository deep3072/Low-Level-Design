from machine import VendingMachine
from coin import Coin
from note import Note

class VendingMachineDemo:
    def start(self):
        vending_machine = VendingMachine()

        print("Filling inventory\n")
        vending_machine.fill_inventory()

        print("Vending Machine is ready to use\n")
        vending_machine.show_inventory()

        # click insert coin/note button
        vending_machine.click_insert_coin_button()

        # insert coins
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)

        # insert note
        vending_machine.insert_note(Note.ONE)
        vending_machine.insert_note(Note.ONE)
        vending_machine.insert_note(Note.ONE)

        # click select item button
        vending_machine.click_select_item_button()

        # choose product
        vending_machine.choose_item(104)

        # updated inventory
        vending_machine.show_inventory()


if __name__ == "__main__":
    demo = VendingMachineDemo()
    demo.start()