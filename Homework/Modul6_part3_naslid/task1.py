class Device:
    def __init__(self, brand, material, purpose, dimensions, price):
        self.brand = brand
        self.material = material
        self.purpose = purpose
        self.__dimensions = dimensions
        self.price = price

    def get_dimensions (self):
        return self.__dimensions
    def put_dimensions (self, dimen):
        self.__dimensions = dimen
    
    def show_info (self):
        print (self.brand, self.material, self.purpose, self.__dimensions, self.price, end= ' ')
        
class CoffeeMachine (Device):
    def __init__(self, brand, material, purpose, dimensions, price, control_type):
        super().__init__(brand, material, purpose, dimensions, price)
        self.control_type = control_type
                
    def get_price (self):
        return self.price
    def put_price (self, price):
        self.price = price          
        
    def show_info (self):
        super().show_info()
        print (self.control_type)

class Blender (Device):
    def __init__(self, brand, material, purpose, dimensions, price, count_of_speeds):
        super().__init__(brand, material, purpose, dimensions, price)
        self.count_of_speeds = count_of_speeds

    def show_info (self):
        super().show_info()
        print (self.count_of_speeds)
        
class MeatGrinder (Device):
    def __init__(self, brand, material, purpose, dimensions, price, reverse):
        super().__init__(brand, material, purpose, dimensions, price)
        self.__reverse = reverse
        
    def get_info_about_reverse (self):
        return self.__reverse
    def put_info_about_reverse (self, reverse):
        self.__reverse = reverse
        
    def show_info (self):
        super().show_info()
        print (self.__reverse)

blender = Blender ('Бренд: Tefal,', 'Матеріал: метал та пластик,', 'Призначення: подрібнення їжі та збивання напоїв,', 4, 'Ціна: 4 299 грн,', 'Кількість швидкостей: мультишвидкісний.')
blender.get_dimensions ()
blender.put_dimensions ('Габарити: 40,6 х 19,2 х 21,5 см,')
blender.get_dimensions ()
blender.show_info ()

coffee_machine = CoffeeMachine ('Бренд: Philips,', 'Матеріал: пластик,', 'Призначення: приготування кавових напоїв,', 'Габарити: 43,3 х 24,6 x 37,1 cм,', 5, 'Тип управління: сенсорний.')
coffee_machine.get_price ()
coffee_machine.put_price ('Ціна: 35 999 грн, зі знижкою - 19 999 грн (-43%),')
coffee_machine.get_price ()
coffee_machine.show_info ()

meat_grinder = MeatGrinder ('Бренд: Bosch,', 'Матеріал: пластик,', 'Призначення: подрібнення м\'яса,', 'Габарити: 25 х 16 х 23 см,', 'Ціна: 5 859 грн, зі знижкою - 4 699 грн (-20%),', 6)
meat_grinder.get_info_about_reverse ()
meat_grinder.put_info_about_reverse ('Наявність реверса: так.')
meat_grinder.get_info_about_reverse ()
meat_grinder.show_info ()