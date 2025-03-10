from log_handler import LogHandler
from log_level import LogLevel

class WarningLogHandler(LogHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler, LogLevel.WARNING)

    def handle(self, level, message):
        if level == self.level:
            print(f"[WARNING] - {message}")
        elif self.next_handler:
            self.next_handler.handle(level, message)