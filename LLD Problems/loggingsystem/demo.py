from log_handler import LogHandler
from log_level import LogLevel
from info_log_handler import InfoLogHandler
from warning_log_handler import WarningLogHandler
from error_log_handler import ErrorLogHandler
from debug_log_handler import DebugLogHandler

class Demo:
    @staticmethod
    def run():
        log_object = InfoLogHandler(WarningLogHandler(DebugLogHandler(ErrorLogHandler(None))))
        log_object.handle(LogLevel.INFO, "For info only")
        log_object.handle(LogLevel.DEBUG, "Debugging...")
        log_object.handle(LogLevel.WARNING, "Take care of warning message")
        log_object.handle(LogLevel.ERROR, "Error happened")


if __name__ == "__main__":
    Demo.run()