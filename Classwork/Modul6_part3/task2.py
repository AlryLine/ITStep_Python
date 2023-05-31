from math import pi

class Square:
    count = 0

    @staticmethod
    def circle (r):
        Square.count += 1
        return pi*r*r

    @staticmethod
    def romb(d1,d2):
        Square.count += 1
        return d1*d2/2

    @staticmethod
    def rectangle (a, b):
        Square.count += 1
        return a*b

    @staticmethod
    def triangle (a, b, c):
        Square.count += 1
        