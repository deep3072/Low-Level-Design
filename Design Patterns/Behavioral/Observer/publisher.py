from abc import ABC, abstractmethod
from subscriber import Subscriber

class Publisher(ABC):
    """
    Subject interface: declare method to add, remove and notify subscribers
    """
    @abstractmethod
    def subscribe(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify_subscriber(self):
        pass