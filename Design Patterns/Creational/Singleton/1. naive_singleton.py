class Singleton:
    # Naive singleton implementation
    _instance = None

    def __new__(cls, value=None): # private constructor simulation
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True

    @staticmethod
    def get_instance(value):
        if Singleton._instance is None:
            Singleton(value)

        return Singleton._instance
    

instance1 = Singleton.get_instance(5)
instance2 = Singleton(10)

if instance1 == instance2:
    print("Both instance are same, Singleton works!")
else:
    print("Singleton does not work!")

print(instance1.value)
print(instance2.value)

# Another way
instance1._instance = Singleton(100) # does not change the value

if id(instance1) == id(instance2):
    print("Both instances have same id.")
else:
    print("singleton does not wok")