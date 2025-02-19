class SharedCharacter:
    """
    Flyweight: Represents the intrinsic state of a character (shared properties)
    """
    def __init__(self, char, font="Arial", size=12, style="normal"):
        self.char = char
        self.font = font
        self.size = size
        self.style = style

    def display(self, position):
        print(f"Displaying '{self.char}' in {self.font}, size {self.size}, {self.style} style at position {position}") # Extrnsic state (position) is provided at runtime
class SharedCharacterFactory:
    """
    FlyweightFactory: Manages the shared characters
    """
    _characters = {}

    @classmethod
    def get_character(cls, char, font="Arial", size=12, style="normal"):
        key = (char, font, size, style) # Use tuple as unique key based on char attributes
        if key not in cls._characters:
            cls._characters[key] = SharedCharacter(char, font, size, style)
            print(f"Creating new character: {key}")
        return cls._characters[key]
    
class Character:
    """
    Client: represent a char in document with extrinsic state
    """
    def __init__(self, shared_character, x, y):
        self.shared_character = shared_character
        self.x = x
        self.y = y

    def draw(self):
        self.shared_character.display((self.x, self.y)) # Delegate to shared character for rendering

text = "Hello world"
document = []

x, y = 0, 0
space = 3

for ch in text:
    shared_char = SharedCharacterFactory.get_character(ch)
    document.append(Character(shared_char, x, y))
    x += space

for char in document:
    char.draw()
