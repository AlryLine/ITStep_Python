class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex (self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex (self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex (self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex ((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(2, 4)
b = Complex(1, 3)

print(a + b)
print(a - b)
print(a * b)
print(a / b)