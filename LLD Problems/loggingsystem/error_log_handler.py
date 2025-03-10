from log_level import LogLevel
from log_handler import LogHandler

class ErrorLogHandler(LogHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler, LogLevel.ERROR)

    def handle(self, level, message):
        if level == self.level:
            print(f"[Error]: {message}")
        else:
            if self.next_handler is not None:
                self.next_handler.handle(level, message)