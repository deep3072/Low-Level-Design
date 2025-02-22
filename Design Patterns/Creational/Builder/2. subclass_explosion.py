class House:
    """
    To overcome lot of parameters in constructor, we can create subclasses for each type of house.
    But this increases subclass and becomes difficult to manage. 
    """
    def __init__(self, windows, doors, rooms):
        self.windows = windows
        self.doors = doors
        self.rooms = rooms
        self.garage = False
        self.garden = False
        self.pool = False
    
    def __repr__(self):
        return f"House(windows={self.windows}, doors={self.doors}, rooms={self.rooms}, garage={self.garage}, garden={self.garden}, pool={self.pool})"
    
class BasicHouse(House):
    """
    Basic house
    """
    def __init__(self, windows, doors, rooms):
        super().__init__(windows, doors, rooms)

class HouseWithGarden(House):
    """
    House with garden
    """
    def __init__(self, windows, doors, rooms):
        super().__init__(windows, doors, rooms)
        self.garden = True

class HouseWithPool(House):
    """
    House with pool
    """
    def __init__(self, windows, doors, rooms):
        super().__init__(windows, doors, rooms)
        self.pool = True

class HouseWithGardenAndPool(HouseWithPool):
    """
    House with garden and pool
    """
    def __init__(self, windows, doors, rooms):
        super().__init__(windows, doors, rooms)
        self.garden = True
        
basic_house = BasicHouse(8, 4, 3)
house_with_pool = HouseWithPool(8, 4, 3)
house_with_garden_pool = HouseWithGardenAndPool(8, 4, 3)

print(basic_house)
print(house_with_pool)
print(house_with_garden_pool)