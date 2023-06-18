class Fraction:
    count = 0
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1
        
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)    
        
    @staticmethod
    def get_count():
        return Fraction.count
    
f1 = Fraction (3,4)
print (str(f1))
f2 = Fraction (2,3)
print (str(f2))
f3 = f1 + f2
f4 = f1 - f2
print (f3)
print (f4)
print (Fraction.get_count ())
    
            