from abc import ABC, abstractmethod

class Color(ABC):
    """
    Implmentor: interface for low level operations
    """
    @abstractmethod
    def apply_color(self):
        pass

class Red(Color):
    """
    Concrete Implementor 1: Red Color
    """
    def apply_color(self):
        print(f"Applying red color...")
    
class Blue(Color):
    """
    Concrete Implementor 2: Blue Color
    """
    def apply_color(self):
        print(f"Applying blue color...")

class Shape(ABC):
    """
    Abstraction: interface for "what to do"
    """
    def __init__(self, color):
        self.color = color # Composition: Shape has a Color
    
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    """
    Refined Abstraction: Circle Shape
    """
    def draw(self):
        print(f"Drawing Circle...")
        self.color.apply_color()
        print(f"Circle drawn with {self.color.__class__.__name__} color.\n")

class Square(Shape):
    """
    Refined Abstraction: Square Shape
    """
    def draw(self):
        print(f"Drawing Square...")
        self.color.apply_color()
        print(f"Circle drawn with {self.color.__class__.__name__} color.\n")

# client code
red = Red()
blue = Blue()

# creating shape objects by injesting a color
circle = Circle(red)
square = Square(blue)

circle.draw()
square.draw()

# also can change the color at runtinme
circle.color = blue
circle.draw()
