from subscriber import Subscriber

class PhoneDisplay(Subscriber):
    """
    Concrete Observer: display the temperature on the phone
    """
    def __init__(self, weather_station):
        self.weather_station = weather_station
    def update(self):
        print(f"Phone Display: The temperature is {self.weather_station.temperature} degrees")