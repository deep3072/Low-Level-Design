from abc import ABC, abstractmethod

class House:
    """
    So the solution of previous 2 problems is to use Builder pattern.
    House: Class representing the end Product.
    """
    def __init__(self):
        self.parts = []
        
    def add(self, part):
        self.parts.append(part)
        
    def __repr__(self):
        return f'House parts: {", ".join(self.parts)}'

class HouseBuilder(ABC):
    """
    Builder interface: Defines the steps needed to build a house
    """
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def  build_windows(self):
        pass
    
    @abstractmethod
    def build_doors(self):
        pass
    
    @abstractmethod
    def build_rooms(self):
        pass
    
    @abstractmethod
    def build_garage(self):
        pass
    
    @abstractmethod
    def build_garden(self):
        pass
    
    @abstractmethod
    def build_pool(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    
class BasicHouseBuilder(HouseBuilder):
    """ 
    Concrete builder 1: Basic house
    """
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.house = House()
    
    def build_doors(self):
        self.house.add("1 door")
    
    def build_windows(self):
        self.house.add("2 windows")
    
    def build_rooms(self):
        self.house.add("1 room")
        
    def build_garage(self):
        pass 
    
    def build_garden(self):
        pass
    
    def build_pool(self):
        pass
    
    def get_result(self):
        return self.house

class LuxuryHouseBuilder(HouseBuilder):
    """ 
    Concrete builder 2: Luxury house
    """
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.house = House()
    
    def build_doors(self):
        self.house.add("2 doors")
    
    def build_windows(self):
        self.house.add("4 windows")
    
    def build_rooms(self):
        self.house.add("3 rooms")
        
    def build_garage(self):
        self.house.add("1 garage")
    
    def build_garden(self):
        self.house.add("1 garden")
        
    def build_pool(self):
        self.house.add("1 pool")
    
    def get_result(self):
        return self.house
    
class HouseDirector:
    """
    Director class: Manages the builders
    """
    def set_builder(self, builder):
        self.builder = builder
    
    def build_basic_house(self):
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_rooms()
        return self.builder.get_result()
    
    def build_luxury_house(self):
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_rooms()
        self.builder.build_garage()
        self.builder.build_garden()
        self.builder.build_pool()
        return self.builder.get_result()
    

# Client code
director = HouseDirector()

basic_builder = BasicHouseBuilder()
director.set_builder(basic_builder)
basic_house = director.build_basic_house()
print("Basic house:", basic_house)

luxury_builder = LuxuryHouseBuilder()
director.set_builder(luxury_builder)
luxury_house = director.build_luxury_house()
print("Luxury house:", luxury_house)
