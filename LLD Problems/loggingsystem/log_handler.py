from abc import ABC, abstractmethod

class LogHandler(ABC):
    def __init__(self, next_handler, level):
        self.level = level
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, level, message):
        pass