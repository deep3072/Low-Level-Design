import time
from threading import Thread

class ThreadUnsafeSingleton:
    """
    The naive singleton implementation fails in multi-threaded environment. This class illustrates that issue.
    """
    _instance = None

    def __new__(cls, value=None):
        if cls._instance is None:
            temp = super().__new__(cls)
            time.sleep(1) # Simulating the time taken to create instance
            cls._instance = temp
            cls._instance._initialized = False
        print("Creating new instance", temp) # 2 different instances createdss
        return cls._instance
    
    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialiazed = True
    
    @staticmethod
    def get_instance(value):
        if not ThreadUnsafeSingleton._instance:
            ThreadUnsafeSingleton(value)
            
        return ThreadUnsafeSingleton._instance

process1 = Thread(target=ThreadUnsafeSingleton, args=(10,))
process2 = Thread(target=ThreadUnsafeSingleton, args=(20,))

process1.start()
process2.start()

    
    