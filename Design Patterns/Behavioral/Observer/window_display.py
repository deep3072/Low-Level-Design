from subscriber import Subscriber

class TVDisplay(Subscriber):
    """
    Concrete Observer: display the temperature on the window
    """
    def __init__(self, weather_station):
        self.weather_station = weather_station
    def update(self):
        print(f"TV Display: The temperature is {self.weather_station.temperature} degrees")