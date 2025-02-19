from abc import ABC, abstractmethod

class Coffee(ABC):
    """
    Component: interface for both original object & decorators
    """
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    """
    Concrete component: original object
    """
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"
    
class CoffeeDecorator(Coffee):
    """
    Decorator: base class for all decorators
    """
    def __init__(self, coffee):
        self._coffee = coffee # Decorator has a reference to the original object

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()
    
class MilkDecorator(CoffeeDecorator):
    """
    Concrete decorator: add milk to the coffee
    """
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return f"{self._coffee.description()}, with milk"
    
class SugarDecorator(CoffeeDecorator):
    """
    Concrete decorator: add sugar to the coffee
    """
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return f"{self._coffee.description()}, with sugar"
    
class WhipDecorator(CoffeeDecorator):
    """
    Concrete decorator: add whip to the coffee
    """
    def cost(self):
        return self._coffee.cost() + 1.5

    def description(self):
        return f"{self._coffee.description()}, with whip"
    
class VanillaDecorator(CoffeeDecorator):
    """
    Concrete decorator: add vanilla to the coffee
    """
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return f"{self._coffee.description()}, with vanilla"
    

my_coffee = SimpleCoffee()
print(f"Description: {my_coffee.description()}, Cost: {my_coffee.cost()}")

my_coffee = MilkDecorator(my_coffee)
print(f"Description: {my_coffee.description()}, Cost: {my_coffee.cost()}")

my_coffee = SugarDecorator(my_coffee)
print(f"Description: {my_coffee.description()}, Cost: {my_coffee.cost()}")