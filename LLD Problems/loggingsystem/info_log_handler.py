from log_handler import LogHandler
from log_level import LogLevel

class InfoLogHandler(LogHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler, LogLevel.INFO)

    def handle(self, level, message):
        if level == self.level:
            print(f"[INFO] - {message}")
        elif self.next_handler:
            self.next_handler.handle(level, message)