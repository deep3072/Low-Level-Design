from log_handler import LogHandler
from log_level import LogLevel

class DebugLogHandler(LogHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler, LogLevel.DEBUG)

    def handle(self, level, message):
        if level == self.level:
            print(f"[DEBUG] - {message}")
        elif self.next_handler:
            self.next_handler.handle(level, message) 