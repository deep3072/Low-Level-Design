from item import Item

class Inventory:
    def __init__(self):
        self.items = {} # structure: {code_number: (Item, quantity)}

    def get_item(self, code_number: int): # return item from code_number
        return self.items.get(code_number, (None, 0))[0]

    def add_item(self, item, quantity: int):
        if item.code_number in self.items:
            self.items[item.code_number] = (item, self.items[item.code_number][1] + quantity)
        else:
            self.items[item.code_number] = (item, quantity)

    def remove_item(self, item):
        try:
            del self.items[item.code_number]
        except KeyError:
            raise ValueError(f"Item {item.code_number} not found in inventory")
        
    def update_sold_item_count(self, code_number: int):
        self.items[code_number] = (self.items[code_number][0], self.items[code_number][1] - 1)
        
    def get_quantity(self, item):
        return self.items.get(item.code_number, (None, 0))[1]
    
    def is_item_available(self, code_number: int):
        return self.items.get(code_number, (None, 0))[1] > 0
    
    def fill_inventory(self, vending_machine):
        
        #create items
        item1 = Item(item_name="Coke", price=2, code_number=101)
        item2 = Item(item_name="Pepsi", price=3, code_number=102)
        item3 = Item(item_name="Lays", price=1.25, code_number=103)
        item4 = Item(item_name="Snickers", price=2.5, code_number=104)
        item5 = Item(item_name="Nuts", price=1.75, code_number=105)

        vending_machine.inventory.add_item(item1, 15)
        vending_machine.inventory.add_item(item2, 15)
        vending_machine.inventory.add_item(item3, 20)
        vending_machine.inventory.add_item(item4, 30)
        vending_machine.inventory.add_item(item5, 10)

    def show_inventory(self, vending_machine):
        print("\nCurrent Inventory:")
        for code_number in vending_machine.inventory.items:
            item = vending_machine.inventory.get_item(code_number)
            quantity = vending_machine.inventory.get_quantity(item)
            print(f"{item.code_number} - {item.item_name} - {quantity}")
        print("\n")