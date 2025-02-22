class House:
    """
    Problem: A class having a constructor with multiple optional parameters. It gets difficult to create objects.
    """
    def __init__(self, windows, doors, rooms, garage=False, garden=False, pool=False):
        self.windows = windows
        self.doors = doors
        self.rooms = rooms
        self.garage = garage
        self.garden = garden
        self.pool = pool

    def __repr__(self):
        return f"House(windows={self.windows}, doors={self.doors}, rooms={self.rooms}, garage={self.garage}, garden={self.garden}, pool={self.pool})"
    

basic_house = House(8, 4, 3, False, False, False)
house_with_garage = House(8, 4, 3, True, False, False)
house_full = House(8, 4, 3, True, True, True)

print(basic_house)
print(house_with_garage)
print(house_full)
