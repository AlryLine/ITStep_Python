class Ship:
    def __init__(self, name, type_of_ship, speed, displacement_tonnage):
        self.name = name
        self.type_of_ship = type_of_ship
        self.speed = speed
        self.__displacement_tonnage = displacement_tonnage
        
    def get_displacement_tonnage (self):
        return self.__displacement_tonnage
    def put_displacement_tonnage (self, dis_tonn):
        self.__displacement_tonnage = dis_tonn
        
    def show_info (self):
        print (self.name, self.type_of_ship, self.speed,  self.__displacement_tonnage)
        
class Frigate (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, battery):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.battery = battery
        
    def show_info_about_battery (self):
        print ('Батарея - основний вогневий тактичний підрозділ в артилерії ракетних, зенітних ракетних, ' 
               'ракетно-артилерійских, а також у берегових військах та надводних кораблях військово-морського флоту.')
        
    def show_info (self):
        super().show_info()
        print (self.battery)
        
class Destroyer (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, additions):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.additions = additions
        
    def get_speed (self):
        return self.speed
    def add_speed (self, s):
        self.speed = s
        
    def show_info (self):
        super().show_info()
        print (self.additions)
        
class Cruiser (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, independence):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.independence = independence
        
    def get_info (self):
        return self.independence
    def add_info (self, i):
        self.independence = i
        
    def show_info (self):
        super().show_info()
        print (self.independence)
        
frigate = Frigate ('Модель корабля: Фрегат.', 'Тип корабля: військове судно.', 
                   'Швидкість: понад 30 вузлів.', 'Водотоннажність: до 4000 тонн.',
                   'Фрегати мають або тільки одну закриту батарею, або одну закриту та одну відкриту на верхній палубі.')
frigate.show_info ()
frigate.show_info_about_battery ()

destroyer = Destroyer ('Модель корабля: Есмінець.', 'Тип корабля: бойовий корабель.',
                       'Швидкість: до 39 вузлів.', 'Водотоннажність: 1500 - 4500 тонн.',
                       'Деякі есмінці мають вертолітний майданчик.')
destroyer.get_speed ()
destroyer.add_speed ('Швидкість: до 40 вузлів.')
destroyer.get_speed ()
destroyer.show_info ()

cruiser = Cruiser ('Модель корабля: Крейсер.', 'Тип корабля: бойовий корабель.',
                   'Швидкість: 36 вузлів.', 'Водотоннажність: в середньому 10000 тонн.', 6)
cruiser.get_info ()
cruiser.add_info ('Такі моделі кораблів є незалежним від загального флоту діючим кораблем.')
cruiser.get_info ()
cruiser.show_info ()