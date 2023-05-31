class Money:
    def __init__(self, bills, pennies):
        self.bills = bills
        self.pennies = pennies

    def get_info_about_bills (self):
        return self.bills
    def put_info_about_bills (self, b):
        self.bills = b

    def get_info_about_pennies (self):
        return self.pennies
    def put_info_about_pennies (self, p):
        self.pennies = p

    def __add__ (self, other):
        a = self.bills + other.bills
        b = self.pennies + other.pennies
        if b > 100:
            a += 1
            b -= 100
        return Money (a,b)

    def __str__(self) -> str:
        return str (self.bills)+ '.' +str (self.pennies)



grn1 = Money (10, 50)
grn2 = Money (20, 75)
print (grn1 + grn2)
