import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle Input
print("Rectangle:")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
r = Rectangle(length, width)
print(f"Rectangle Area: {r.area()}")
print(f"Rectangle Perimeter: {r.perimeter()}")

# Circle Input
print("\nCircle:")
radius = float(input("Enter radius: "))
c = Circle(radius)
print(f"Circle Area: {c.area()}")
print(f"Circle Perimeter: {c.perimeter()}")
