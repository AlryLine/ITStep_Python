class Stadium:
    def __init__ (self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.__city = city
        self.capacity = capacity
    
    def get_city (self):
        return self.__city
    def put_city (self, city):
        self.__city = city
        
    def __str__ (self):
        return f'Вмісткість глядачів: {self.capacity}'   

    def get_info (self):
        return (self.name, self.year, self.country, self.city, self.__capacity)
    def show_info (self):
        print ('Є такий відомий стадіон:')

stadium = Stadium ('"Уемблі"', 2007, 'Велика Британія', 4, 90000)
stadium.show_info ()
stadium.put_city ('Лондон')
print ('Назва:', stadium.name)
print ('Рік відкриття:', stadium.year)
print ('Країна:', stadium.country)
print ('Місто:', stadium.get_city())
print (str(stadium))