class Airplane:
    def __init__(self, model, current_passengers, max_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, other):
        new_passengers = self.current_passengers + other
        if new_passengers > self.max_passengers:
            print ("Дуже багато пасажирів!")
        return Airplane(self.model, self.max_passengers, new_passengers)

    def __sub__(self, other):
        new_passengers = self.current_passengers - other
        if new_passengers < 0:
            print ("Недостатньо пасажирів!")
        return Airplane(self.model, self.max_passengers, new_passengers)

    def __iadd__(self, other):
        self.current_passengers += other
        if self.current_passengers > self.max_passengers:
            print ("Дуже багато пасажирів!")
        return self

    def __isub__(self, other):
        self.current_passengers -= other
        if self.current_passengers < 0:
            print ("Недостатньо пасажирів!")
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"{self.model} ({self.current_passengers}/{self.max_passengers})"
    
airplane1 = Airplane ("Boeing 747", 250, 500)
airplane2 = Airplane ("Airbus A300", 400, 850)

print(airplane1 == airplane2)
print(airplane1 < airplane2)
print ()
airplane1 += 200
print(airplane1)
print ()
airplane2 -= 100
print(airplane2)
print ()
airplane1 = airplane1 + 250
print(airplane1)
print ()
airplane2 = airplane2 - 350
print(airplane2)
print ()
print (airplane1 >= airplane2)  