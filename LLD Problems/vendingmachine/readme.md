# Design a Vending Machine

## Requirements

1. The vending machine should have multiple products with different prices and quantities.
2. The vending machine should accept coins and notes of various denominations.
3. Users should be able to select items by entering product code number.
4. The vending machine should be able to calculate the total payment and handle insufficient payments or out-of-stock scenarios.
5. The vending machine should return change if the amount paid exceeds the item price.
6. It should provide an interface to add, remove, and update items in the inventory.


## Classes, Interfaces, and Enums

1. The `Item` class represents a product in the vending machine, with properties such as name, price, and code number.
2. The `Coin` and `Note` enums represent the different denominations of coins and notes accepted by the vending machine.
3. The `Inventory` class manages the available products and their quantities in the vending machine.
4. The `State` interface defines the behavior of the vending machine in different states, such as idle, has money, selection, and dispense.
5. The `IdleState`, `HasMoneyState`, `SelectionState`, and `DispenseState` classes implement the `State` interface and define the specific behaviors for each state.
6. The `VendingMachine` class is the main class that represents the vending machine. It maintains the current state, selected product, total payment, and provides methods for state transitions and payment handling.
7. The `VendingMachineDemo` class demonstrates the usage of the vending machine by adding products to the inventory, selecting products, inserting coins and notes, dispensing products, and returning change.