class Auto:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
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
        
    def __str__ (self):
        return f'Рік випуску: {self.year}'
    
    def get_info (self):
        return (self.model, self.year, self.manufacturer, self.engine_volume, self.color, self.__price)
    def show_info (self):
        print ('Представляю вам автомобіль: ')
    
auto = Auto('Lamborgini Huracan', 2014, 'Lamborgini', '5 літрів', 'хамелеон', 6)

auto.show_info ()
auto.put_price (230000)
print ('Модель автомобіля:', auto.model)
print (str(auto))
print ('Виробник:', auto.manufacturer)
print ('Об\'єм двигуна:', auto.engine_volume)
print ('Колір:', auto.color)
print ('Ціна:', auto.get_price(),'$')
