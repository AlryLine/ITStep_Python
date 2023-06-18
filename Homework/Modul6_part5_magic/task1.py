class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return 2 * 3.14 * self.radius > 2 * 3.14 * other.radius
    
    def __lt__(self, other):
        return 2 * 3.14 * self.radius < 2 * 3.14 * other.radius
    
    def __le__(self, other):
        return 2 * 3.14 * self.radius <= 2 * 3.14 * other.radius
    
    def __ge__(self, other):
        return 2 * 3.14 * self.radius >= 2 * 3.14 * other.radius
    
    def __add__(self, other):
        return Circle (self.radius + other.radius)
    
    def __sub__(self, other):
        return Circle (self.radius - other.radius)
    
    def __iadd__(self, other):
        self.radius += other.radius
        return self
    
    def __isub__(self, other):
        self.radius -= other.radius
        return self
    
    def get_area(self):
        return 3.14 * self.radius ** 2
    
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    
circle1 = Circle (10)
circle2 = Circle (7)
print (circle1.get_area ())
print (circle2.get_area ())
print (circle1.get_circumference ())
print (circle2.get_circumference ())
print (circle1 == circle2)
print (circle1 >= circle2)
circle3 = circle1.__add__(circle2)
print (circle3.radius)
circle4 = circle1.__sub__(circle2)
print (circle4.radius) 
circle5 = circle3.__iadd__(circle1)
print (circle5.radius)
circle6 = circle5.__isub__(circle4)
print (circle6.radius)  