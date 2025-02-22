from threading import Thread, Lock

class SingletonMeta(type):
    """
    Metaclass implementation for Singleton pattern.
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        This method is called when an instance of the class is created. If an instance of class does not exist,
        it creates one and stores it in _instance dict. Else, it return the exisiting instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            print(cls._instances[cls].value)
            return cls._instances[cls]
        
class Singleton(metaclass=SingletonMeta):
    """
    Singleton class using SingletonMeta metaclass.
    """
    def __init__(self, value):
        self.value = value

print("If both values are 5 then Singleton works! Otherwise, Singleton does not work!\n")
        
process1 = Thread(target=Singleton, args=("5",))
process2 = Thread(target=Singleton, args=("10",))

process1.start()
process2.start()

# if instance1 == instance2:
#     print("Both instances are same")
# else:
#     print("Singleton Meta does not work!")
    
# print(instance1.value) # 5
# print(instance2.value) # 5