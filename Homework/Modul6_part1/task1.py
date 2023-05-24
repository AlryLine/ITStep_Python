class Auto:
    def __init__(self, model, year, manufacturer, engine_volume, color, price = 0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.__price = price
    
    def get_price (self):
        return self.__price
    def put_price (self, price):
        self.__price = price

    def show_info (self):
        return (self.model, self.year, self.manufacturer, self.engine_volume, self.color, self.__price)
    
auto = Auto(1, 2, 3, 4, 5, 6)
auto.model = 'Lamborgini Huracan'
auto.year = 2014
auto.manufacturer = 'Lamborgini'
auto.engine_volume = 5
auto.color = 'хамелеон'
auto.put_price (230000)

print ('Модель автомобіля: ', auto.model)
print ('Рік випуску: ', auto.year)
print ('Виробник: ', auto.manufacturer)
print ('Об\'єм двигуна: ', auto.engine_volume,'літрів')
print ('Колір: ', auto.color)
print ('Ціна: ', auto.get_price(),'$')
