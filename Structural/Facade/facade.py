class CardReader:
    def read_card(self):
        print("Reading card...")
        return "valid_card_data"
    
class PINValidator:
    def validate_pin(self, card_data, pin):
        print(f"Validating PIN: {pin}")
        # PIN validation logic
        return True
    
class AccountManager:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 1000.0 # start balance

    def check_balance(self):
        print("Checking account balance...")
        return 1000.0
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawing ${amount}. New balance: ${self.balance}")
            return True
        else:
            print("Insufficient funds.")
            return False
        
class CashDispenser:
    def dispense_cash(self, amount):
        print(f"Dispensing ${amount} cash.")

class ATMFacade:
    """
    Facade interface to simplify the ATM operations
    """
    def __init__(self):
        self.card_reader = CardReader()
        self.pin_validator = PINValidator()
        self.account_manager = AccountManager("123456789")
        self.cash_dispenser = CashDispenser()

    def withdraw_cash(self, pin, amount):
        print("Starting ATM transaction...")
        card_data = self.card_reader.read_card()
        if not card_data:
            print("Card reading failed.")
            return False
        
        if not self.pin_validator.validate_pin(card_data, pin):
            print("Invalid PIN.")
            return False
        
        balance = self.account_manager.check_balance()
        
        if self.account_manager.withdraw(amount):
            self.cash_dispenser.dispense_cash(amount)
            print("Transaction completed successfully.\n")
            return True
        else:
            print("Transaction failed.\n")
            return False
        
atm = ATMFacade()
atm.withdraw_cash("1234", 100)

atm.withdraw_cash("1234", 1000)