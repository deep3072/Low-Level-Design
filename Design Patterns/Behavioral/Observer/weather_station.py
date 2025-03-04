from publisher import Publisher

class WeatherStation(Publisher):
    """
    Concrete Publisher(Subject): maintain a list of subscribers and notify them of changes
    """
    def __init__(self):
        self._subscribers = set()
        self._temperature = None

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscriber(self):
        for subscriber in self._subscribers:
            subscriber.update()

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature
        self.notify_subscriber()