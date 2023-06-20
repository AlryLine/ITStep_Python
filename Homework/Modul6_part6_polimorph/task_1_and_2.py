import math

class Figure:
    def find_area (self):
        pass
    
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height
    
    def __int__(self):
        return int(self.find_area())
    
    def __str__(self):
        return f'Прямокутник з шириною {self.width} та висотою {self.height}.'

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return math.pi * self.radius ** 2
    
    def __int__(self):
        return int(self.find_area())
    
    def __str__(self):
        return f'Круг з радіусом {self.radius}.'

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        return 0.5 * self.base * self.height
    
    def __int__(self):
        return int(self.find_area())
    
    def __str__(self):
        return f'Прямокутний трикутник з довжиною основи {self.base} та висотою {self.height}.'

class Trapezium(Figure):
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def find_area(self):
        return 0.5 * (self.a + self.b) * self.height
    
    def __int__(self):
        return int(self.find_area())
    
    def __str__(self):
        return f'Трапеція зі сторонами {self.a} та {self.b}, та висотою {self.height}.' 
    
rectangle = Rectangle(6, 12)
print (str(rectangle))
print("Площа прямокутника:", rectangle.find_area())
print ()
circle = Circle(2)
print (str(circle))
print("Площа круга:", circle.find_area())
print ()
triangle = RightTriangle(4, 5)
print (str(triangle))
print("Площа прямокутного трикутника:", triangle.find_area())
print ()
trapezium = Trapezium(2, 6, 8)
print (str(trapezium))
print("Площа трапеції:", trapezium.find_area())      