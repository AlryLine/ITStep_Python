class Counter:
    __count = 0

    @staticmethod
    def maximum (a, b, c, d):
        mx = [a, b, c, d]
        Counter.__count += 1
        return max(mx)

    @staticmethod
    def minimum (a, b, c, d):
        mn = [a, b, c, d]
        Counter.__count += 1
        return min(mn)

    @staticmethod
    def middle_ariphmetic (a, b, c, d):
        Counter.__count += 1
        return (a + b + c + d)/4

    @staticmethod
    def factorial (a):
        Counter.__count += 1
        fact = 1
        for i in range (1, a+1):
            fact *= i
        return fact

    @staticmethod
    def get_count():
        return Counter.__count


e = Counter.maximum(1, 7, 5, 2)
print ("Max: ", e)
f = Counter.minimum (2, -1, 5, 3)
print ("Min", f)
g = Counter.middle_ariphmetic (1, 3, 6, 2)
print ("Middle ariphmetic: ", g)
h = Counter.factorial (5)
print ("Factorial: ", h)
print ("Count: ", Counter.get_count())