class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1
        
    @staticmethod
    def get_count():
        return Fraction.count
    
            