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
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, sails, battery):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.sails = sails
        self.battery = battery
        
    def info_about_frigate (self):
        print ('Корабель №1:')    
        
    def show_info_about_battery (self):
        print ('Батарея - основний вогневий тактичний підрозділ в артилерії ракетних, зенітних ракетних,\nракетно-артилерійских, а також у берегових військах та надводних кораблях військово-морського флоту.')
        
    def raise_the_sails (self, sails):
        print ('Команда підняти або опустити вітрила фрегату:')    
        if sails == 'підняти вітрила':
            print ('Вітрила підняті!')
        elif sails == 'опустити вітрила':
            print ('Вітрила опущені!')
                
    def show_info (self):
        super().show_info()
        print (self.sails, self.battery)
        
class Destroyer (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, additions):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.additions = additions
        
    def info_about_destroyer (self):
        print ('Корабель №2:')    
             
    def __str__(self):
        return f' Швидкість: до {self.speed} вузлів.'    
        
    def show_info (self):
        super().show_info()
        print (self.additions)
        
class Cruiser (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, independence):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.__independence = independence
        
    def get_info (self):
        return self.__independence
    def add_info (self, i):
        self.__independence = i
    
    def info_about_cruiser (self):
        print ('Корабель №3:')    
        
    def show_info (self):
        super().show_info()
        print (self.__independence)
        
frigate = Frigate (' Модель: Фрегат.\n','Тип: військове судно.\n','Швидкість: понад 30 вузлів.\n','Водотоннажність: до 4000 тонн.',' Наявність вітрил: може мати вітрила.','\nОсобливості:\n Фрегати мають або тільки одну закриту батарею, або одну закриту та одну відкриту на верхній палубі.')
frigate.info_about_frigate ()
frigate.show_info ()
print ()
frigate.show_info_about_battery ()
print()
frigate.raise_the_sails ('підняти вітрила')
print ()
destroyer = Destroyer ('Есмінець.','бойовий корабель.',40,4,'Деякі есмінці мають вертолітний майданчик.')
destroyer.put_displacement_tonnage ('1500 - 4500 тонн.')
destroyer.info_about_destroyer ()
print (' Модель:', destroyer.name)
print (' Тип:', destroyer.type_of_ship)
print (str(destroyer))
print (' Водотоннажність:', destroyer.get_displacement_tonnage())
print ('Доповнення:\n', destroyer.additions)
print ()
cruiser = Cruiser (' Модель: Крейсер.\n','Тип: бойовий корабель.\n','Швидкість: 36 вузлів.\n','Водотоннажність: в середньому 10000 тонн.',6)
cruiser.get_info ()
cruiser.add_info ('Особливості:\n Такі моделі кораблів є незалежним від загального флоту діючим кораблем.')
cruiser.get_info ()
cruiser.info_about_cruiser ()
cruiser.show_info ()