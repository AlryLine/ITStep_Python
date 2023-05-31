class Stadium:
    def __init__ (self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.__capacity = capacity
    
    def get_capacity (self):
        return self.__capacity
    def put_capacity (self, count):
        self.__capacity = count

    def get_info (self):
        return (self.name, self.year, self.country, self.city, self.__capacity)
    def show_info (self):
        print ('Є такий відомий стадіон:')

stadium = Stadium ('"Уемблі"', 2007, 'Велика Британія', 'Лондон', 5)
stadium.show_info ()
stadium.put_capacity (90000)
print ('Назва:', stadium.name)
print ('Рік відкриття:', stadium.year)
print ('Країна:', stadium.country)
print ('Місто:', stadium.city)
print ('Вмісткість глядачів:', stadium.get_capacity())