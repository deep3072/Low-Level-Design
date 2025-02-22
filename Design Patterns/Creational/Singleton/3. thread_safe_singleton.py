from threading import Thread, Lock
import time

class ThreadSafeSingleton:
    """
    This class implements a thread-safe singleton pattern.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls, value=None):
        with cls._lock:
            if cls._instance is None:
                temp = super().__new__(cls)
                time.sleep(1)
                cls._instance = temp
                cls._instance._initialized = False
            print("Creating instance", cls._instance) # only 1 instance created
        return cls._instance

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True
    
    @staticmethod
    def get_instance(value):
        if not ThreadSafeSingleton._instance:
            ThreadSafeSingleton(value)
        return ThreadSafeSingleton._instance

p1 = Thread(target=ThreadSafeSingleton, args=(10,))
p2 = Thread(target=ThreadSafeSingleton, args=(20,))

p1.start()
p2.start()