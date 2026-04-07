# super() = Function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, name, filled):
        self.color = color
        self.name= name
        self.filled = filled
    
    def describe(self):
        return f"{self.color} {self.name} is {'colored' if self.filled else 'uncolored'}"

class Circle(Shape):
    def __init__(self, color, name, filled, radius):
        super().__init__(color, name, filled)
        self.radius = radius
    
    def describe(self):
        return f"{super().describe()} and radius is {self.radius}."
    
    def area(self):
        return f"Area: {3.14 * self.radius ** 2}" 

class Square(Shape):
    def __init__(self, color, name, filled, width):
        super().__init__(color, name, filled)
        self.width = width

    def describe(self):
        return f"{super().describe()} and width is {self.width}."

class Triangle(Square):
    def __init__(self, color, name, filled, width, height):
        super().__init__(color, name, filled, width)
        self.height = height

    def describe(self):
        return f"{super().describe()} plus height is {self.height}."
    

circle = Circle("Blue", "Circle", False, 11)
square = Square("Red", "Square", True, 33)
triangle = Triangle("Black", "Triangle", True, 20, 10)

print(circle.describe())
print(circle.area())
print(square.describe())
print(triangle.describe())