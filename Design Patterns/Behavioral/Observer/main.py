from weather_station import WeatherStation
from phone_display import PhoneDisplay
from window_display import TVDisplay

def main():
    station = WeatherStation()

    phone = PhoneDisplay(station)
    tv = TVDisplay(station)

    station.subscribe(phone)
    station.subscribe(tv)

    station.temperature = 25
    station.temperature = 30

    print("Removing phone ...\n")

    station.unsubscribe(phone)
    station.temperature = 35

if __name__ == "__main__":
    main()