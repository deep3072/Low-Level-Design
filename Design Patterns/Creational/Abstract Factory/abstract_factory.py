from abc import ABC, abstractmethod

class Chair(ABC):
    """
    Abstract Product 1: an interface for Chair objects.
    """
    @abstractmethod
    def sit_on(self):
        pass

    @abstractmethod
    def has_legs(self):
        pass

class CoffeeTable(ABC):
    """
    Abstract Product 2: an interface for Coffee Table objects.
    """
    @abstractmethod
    def put_on(self):
        pass

    @abstractmethod
    def has_legs(self):
        pass

class ModernChair(Chair):
    """
    Concrete Product 1: Implements the Chair interface with Modern Chair functionality.
    """
    def sit_on(self):
        return "Sit on a modern chair"
    
    def has_legs(self):
        return "Modern chair has 4 legs"
    
class ModernCoffeeTable(CoffeeTable):
    """
    Concrete Product 2: Implements the Coffee Table interface with Modern Coffee Table functionality.
    """
    def put_on(self):
        return "Put on a modern coffee table"
    
    def has_legs(self):
        return "Modern coffee table has 4 legs"

class VictorianChair(Chair):
    """
    Concrete Product 3: Implements Chair interface with Victorian Chair functionality.
    Define behavior specific to Victorian chairs.
    """
    def sit_on(self):
        return "Sit on a victorian chair"
    
    def has_legs(self):
        return "Victorian chair has 3 legs"
    
class VictorianCoffeeTable(CoffeeTable):
    """
    Concrete Product 4: Coffee Table interface with Victorian Coffee Table functionality.
    """
    def put_on(self):
        return "Put on a victorian coffee table"
    
    def has_legs(self):
        return "Victorian coffee table has 3 legs"

class FurnitureFactory(ABC):
    """
    Abstract Factory: Factory of Factories
    """
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_coffee_table(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    """
    Concrete Factory 1: Implements the operations to create concrete modern product objects.
    """
    def create_chair(self):
        return ModernChair()
    
    def create_coffee_table(self):
        return ModernCoffeeTable()
    
class VictorianFurnitureFactory(FurnitureFactory):
    """
    Concrete Factory 2: Implements the operations to create concrete victorian product objects.
    """
    def create_chair(self):
        return VictorianChair()
    
    def create_coffee_table(self):
        return VictorianCoffeeTable()

def client(factory):
    chair = factory.create_chair()
    coffee_table = factory.create_coffee_table()
    print(f"{chair.sit_on()}\n{chair.has_legs()}\n")
    print(f"{coffee_table.put_on()}\n{coffee_table.has_legs()}\n")

print("-------->")
print("Create Moderm Furniture")
client(ModernFurnitureFactory())

print("-------->")
print("Create Victorian Furniture")
client(VictorianFurnitureFactory())